import re
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class LegifranceClient:
    """Client pour l'API Légifrance via la plateforme PISTE."""
    
    TOKEN_URL = "https://oauth.piste.gouv.fr/api/oauth/token"
    API_BASE_URL = "https://api.piste.gouv.fr/dila/legifrance/lf-engine-app"

    def __init__(self, client_id=None, client_secret=None):
        self.client_id = client_id or os.getenv("PISTE_CLIENT_ID")
        self.client_secret = client_secret or os.getenv("PISTE_CLIENT_SECRET")
        self.access_token = None

    def authenticate(self):
        """Obtient un jeton OAuth2 en utilisant Basic Auth."""
        data = {
            "grant_type": "client_credentials",
            "scope": "openid"
        }
        response = requests.post(
            self.TOKEN_URL, 
            data=data, 
            auth=(self.client_id, self.client_secret)
        )
        response.raise_for_status()
        self.access_token = response.json().get("access_token")
        return self.access_token

    def _get_headers(self):
        if not self.access_token:
            self.authenticate()
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def find_code_id(self, code_name):
        """Trouve le LEGITEXT d'un code par son nom."""
        url = f"{self.API_BASE_URL}/list/code"
        payload = {
            "pageNumber": 1,
            "pageSize": 200,
            "states": ["VIGUEUR"]
        }
        
        try:
            response = requests.post(url, json=payload, headers=self._get_headers())
            if response.status_code == 200:
                codes = response.json().get("results", [])
                code_keywords = [w.lower() for w in code_name.split() if len(w) > 3 and w.lower() not in ["code", "du", "de", "la", "le", "des", "l"]]
                
                for code in codes:
                    titre = code.get("titre", "").lower()
                    matches = sum(1 for kw in code_keywords if kw in titre)
                    if matches >= min(2, len(code_keywords)):
                        return code.get("titre")
        except Exception as e:
            print(f"  Erreur find_code_id: {e}")
        return None
    
    def search_article(self, article_num, code_name, fond="CODE_ETAT"):
        """Recherche l'ID d'un article dans un code spécifique.
        
        Args:
            article_num: Numéro de l'article à rechercher
            code_name: Nom du code
            fond: Type de fond à utiliser ("CODE_ETAT" ou "CODE_DATE")
        """
        clean_num_match = re.search(r"[L|R|D]?\.?\s?\d+(?:[-─]\d+)*", article_num, re.IGNORECASE)
        clean_num = clean_num_match.group(0).replace(".", "").replace(" ", "") if clean_num_match else article_num
        
        exact_code_name = self.find_code_id(code_name)
        if not exact_code_name:
            exact_code_name = code_name
        
        url = f"{self.API_BASE_URL}/search"
        payload = {
            "recherche": {
                "champs": [
                    {
                        "typeChamp": "NUM_ARTICLE",
                        "criteres": [{"typeRecherche": "EXACTE", "valeur": clean_num, "operateur": "ET"}],
                        "operateur": "ET"
                    }
                ],
                "filtres": [{
                    "facette": "NOM_CODE",
                    "valeurs": [exact_code_name]
                }],
                "pageNumber": 1,
                "pageSize": 10,
                "operateur": "ET",
                "sort": "PERTINENCE",
                "typePagination": "ARTICLE"
            },
            "fond": fond
        }
        
        try:
            response = requests.post(url, json=payload, headers=self._get_headers())
            if response.status_code == 200:
                data = response.json()
                results = data.get("results", [])
                if results:
                    for result in results:
                        sections = result.get("sections", [])
                        for section in sections:
                            extracts = section.get("extracts", [])
                            for extract in extracts:
                                article_id = extract.get("id", "")
                                if article_id.startswith("LEGIARTI"):
                                    return article_id
        except Exception as e:
            print(f"  DEBUG Error: {e}")
        return None

    def get_article_content(self, article_id, expected_num=None, expected_code=None):
        """Récupère le contenu brut d'un article avec vérifications."""
        url = f"{self.API_BASE_URL}/consult/getArticle"
        payload = {"id": article_id}
        
        response = requests.post(url, json=payload, headers=self._get_headers())
        response.raise_for_status()
        data = response.json()
        
        article = data.get("article", {})
        article_num = article.get("num", "")
        article_text = article.get("texte", "")
        
        context = data.get("context", {})
        text_title = context.get("textTitle", "")
        
        if expected_num and article_num:
            clean_expected = expected_num.replace(" ", "").replace(".", "").replace("-", "").upper()
            clean_actual = article_num.replace(" ", "").replace(".", "").replace("-", "").upper()
            if clean_expected not in clean_actual and clean_actual not in clean_expected:
                return {"num": article_num, "texte": article_text, "code": text_title, "mismatch": True}
        
        if expected_code and text_title:
            code_keywords = [w.lower() for w in expected_code.split() if len(w) > 3 and w.lower() not in ["code", "du", "de", "la", "le", "des"]]
            text_title_lower = text_title.lower()
            matches = sum(1 for kw in code_keywords if kw in text_title_lower)
            if matches < min(2, len(code_keywords)):
                return {"num": article_num, "texte": article_text, "code": text_title, "mismatch": True}
        
        return {"num": article_num, "texte": article_text, "code": text_title, "mismatch": False}
