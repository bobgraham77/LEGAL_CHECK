import re
import requests
import json
import os
from datetime import datetime
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
        # Utilisation de l'authentification Basic (Client ID, Client Secret)
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
            "states": ["VIGUEUR"]  # Seulement les codes en vigueur
        }
        
        try:
            response = requests.post(url, json=payload, headers=self._get_headers())
            if response.status_code == 200:
                codes = response.json().get("results", [])
                code_keywords = [w.lower() for w in code_name.split() if len(w) > 3 and w.lower() not in ["code", "du", "de", "la", "le", "des", "l"]]
                
                for code in codes:
                    titre = code.get("titre", "").lower()
                    # Vérifier si au moins 2 mots-clés correspondent
                    matches = sum(1 for kw in code_keywords if kw in titre)
                    if matches >= min(2, len(code_keywords)):
                        print(f"  Code trouvé: {code.get('titre')} ({code.get('cid')})")
                        return code.get("titre")  # Retourner le titre exact
        except Exception as e:
            print(f"  Erreur find_code_id: {e}")
        return None
    
    def search_article(self, article_num, code_name):
        """
        Recherche en 2 étapes : 1) Trouver le code, 2) Chercher l'article dedans.
        """
        clean_num_match = re.search(r"[L|R|D]?\.?\s?\d+(?:[-─]\d+)*", article_num, re.IGNORECASE)
        clean_num = clean_num_match.group(0).replace(".", "").replace(" ", "") if clean_num_match else article_num
        
        print(f"DEBUG: Recherche Article='{clean_num}' dans Code='{code_name}'")
        
        # Étape 1 : Trouver le titre exact du code
        exact_code_name = self.find_code_id(code_name)
        if not exact_code_name:
            exact_code_name = code_name  # Fallback sur le nom fourni
        
        url = f"{self.API_BASE_URL}/search"
        
        # Recherche avec filtre sur le LEGITEXT du code si trouvé
        payload = {
            "recherche": {
                "champs": [
                    {
                        "typeChamp": "NUM_ARTICLE",
                        "criteres": [{"typeRecherche": "EXACTE", "valeur": clean_num, "operateur": "ET"}],
                        "operateur": "ET"
                    }
                ],
                "pageNumber": 1,
                "pageSize": 10,
                "sort": "PERTINENCE",
                "typePagination": "DEFAUT"
            },
            "fond": "CODE_ETAT"
        }
        
        # Ajouter le filtre : nom exact du code
        payload["recherche"]["filtres"] = [
            {
                "facette": "TEXT_NOM_CODE",
                "valeurs": [exact_code_name]
            }
        ]
        
        try:
            response = requests.post(url, json=payload, headers=self._get_headers())
            if response.status_code == 200:
                data = response.json()
                results = data.get("results", [])
                if results:
                    # Les articles sont dans result.sections[].extracts[]
                    for result in results:
                        sections = result.get("sections", [])
                        for section in sections:
                            extracts = section.get("extracts", [])
                            for extract in extracts:
                                article_id = extract.get("id", "")
                                if article_id.startswith("LEGIARTI"):
                                    print(f"  ✓ Article trouvé : {article_id}")
                                    return article_id
        except Exception as e:
            print(f"  DEBUG Error: {e}")
        
        return None

    def _fallback_search(self, clean_num, code_name):
        url = f"{self.API_BASE_URL}/search"
        payload = {
            "recherche": {
                "champs": [
                    {"typeChamp": "NUM_ARTICLE", "criteres": [{"typeRecherche": "EXACTE", "valeur": clean_num, "operateur": "ET"}], "operateur": "ET"}
                ],
                "filtres": [
                    {
                        "facette": "NOM_CODE",
                        "valeurs": [code_name]
                    }
                ],
                "pageNumber": 1,
                "pageSize": 10,
                "sort": "PERTINENCE",
                "typePagination": "ARTICLE"
            },
            "fond": "CODE_ETAT"
        }
        try:
            res = requests.post(url, json=payload, headers=self._get_headers())
            if res.status_code == 200:
                results = res.json().get("results", [])
                code_keywords = [w.lower() for w in code_name.split() if len(w) > 3]
                
                for result in results:
                    sections = result.get("sections", [])
                    for section in sections:
                        extracts = section.get("extracts", [])
                        for extract in extracts:
                            article_id = extract.get("id", "")
                            if article_id.startswith("LEGIARTI"):
                                # Vérifier correspondance avec le numéro
                                if clean_num.replace("-", "").replace(".", "").upper() in article_id or \
                                   extract.get("title", "").upper().find(clean_num.upper()) >= 0:
                                    print(f"  ✓ Article trouvé (fallback) : {article_id}")
                                    return article_id
        except: pass
        return None

    def get_article_content(self, article_id, expected_num=None, expected_code=None):
        """Récupère le contenu brut d'un article par son ID avec vérification du numéro ET du code."""
        url = f"{self.API_BASE_URL}/consult/getArticle"
        payload = {"id": article_id}
        
        response = requests.post(url, json=payload, headers=self._get_headers())
        response.raise_for_status()
        data = response.json()
        
        article = data.get("article", {})
        article_num = article.get("num", "")
        article_text = article.get("texte", "")
        
        # Récupérer le code parent
        context = data.get("context", {})
        text_title = context.get("textTitle", "")
        
        # Vérification 1 : le numéro d'article doit correspondre
        if expected_num and article_num:
            clean_expected = expected_num.replace(" ", "").replace(".", "").replace("-", "").upper()
            clean_actual = article_num.replace(" ", "").replace(".", "").replace("-", "").upper()
            
            if clean_expected not in clean_actual and clean_actual not in clean_expected:
                print(f"  ⚠️ Numéro incorrect: {article_num} ≠ {expected_num}")
                return {"num": article_num, "texte": article_text, "code": text_title, "mismatch": True}
        
        # Vérification 2 : le code doit correspondre
        if expected_code and text_title:
            # Extraire les mots-clés du code attendu
            code_keywords = [w.lower() for w in expected_code.split() if len(w) > 3 and w.lower() not in ["code", "du", "de", "la", "le", "des"]]
            text_title_lower = text_title.lower()
            
            # Au moins 2 mots-clés doivent correspondre
            matches = sum(1 for kw in code_keywords if kw in text_title_lower)
            if matches < min(2, len(code_keywords)):
                print(f"  ⚠️ Code incorrect: '{text_title}' ≠ '{expected_code}'")
                return {"num": article_num, "texte": article_text, "code": text_title, "mismatch": True}
        
        return {"num": article_num, "texte": article_text, "code": text_title, "mismatch": False}

class LegalParser:
    """Parseur Regex pour extraire les citations juridiques."""
    
    # Mapping des abréviations vers les noms complets de codes Légifrance
    CODE_MAPPING = {
        "CASF": "Code de l'action sociale et des familles",
        "CJA": "Code de justice administrative",
        "CSS": "Code de la sécurité sociale",
        "CRPA": "Code des relations entre le public et l'administration",
        "CP": "Code pénal",
        "CC": "Code civil",
        "CT": "Code du travail"
    }

    # Regex simplifiée mais robuste pour capturer le numéro et le code
    ARTICLE_PATTERN = r"(?i)article\s+([L|R|D]?\.?\s?\d+(?:[-─]\d+)*[a-z]*)\s+du\s+((?:Code\s+[^,\.;\n]+?)|(?:[A-Z]{2,}))(?=\s+(?:prévoit|dispose|stipule|est|doit|peut|a)|[\.,;]|$)"

    @classmethod
    def extract_citations(cls, text):
        citations = []
        matches = re.finditer(cls.ARTICLE_PATTERN, text, re.IGNORECASE)
        for match in matches:
            article_num = match.group(1).strip()
            code_raw = match.group(2).strip()
            
            # Nettoyage très strict du code raw (suppression Markdown, verbes, etc.)
            # On enlève les étoiles Markdown
            code_clean = code_raw.replace("*", "").strip()
            # On coupe dès qu'on voit un verbe ou un mot suspect de fin de nom de code
            stop_words = ["prévoit", "dispose", "stipule", "est", "doit", "peut", "impose", "subordonne", "prévoit", "relatif"]
            for word in stop_words:
                if f" {word} " in f" {code_clean.lower()} ":
                    code_clean = re.split(f" {word} ", code_clean, flags=re.IGNORECASE)[0].strip()
            
            # Normalisation du code
            code_name = cls.CODE_MAPPING.get(code_clean.upper(), code_clean)
            
            citations.append({
                "full_match": match.group(0),
                "article_num": article_num,
                "code_name": code_name,
                "context": text[max(0, match.start()-100):min(len(text), match.end()+100)]
            })
        return citations

class ComplianceChecker:
    """Moteur de préparation pour analyse externe."""
    pass

def main(input_md_path):
    with open(input_md_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Extraction Regex
    print("Étape 1 : Extraction des citations...")
    citations = LegalParser.extract_citations(content)
    print(f"Trouvé {len(citations)} citations.")
    
    # 2. Légifrance API
    print("Étape 2 : Consultation Légifrance...")
    legifrance = LegifranceClient()
    
    analysis_task = []
    
    for cit in citations:
        print(f"Récupération de {cit['full_match']}...")
        try:
            art_id = legifrance.search_article(cit['article_num'], cit['code_name'])
            if not art_id:
                print(f"Article non trouvé sur Légifrance : {cit['article_num']}")
                continue
            
            # Récupérer le contenu avec vérification du numéro ET du code
            article_data = legifrance.get_article_content(art_id, cit['article_num'], cit['code_name'])
            
            # Vérifier si le numéro ou le code ne correspondent pas
            if article_data.get("mismatch"):
                print(f"  ⚠️ Article ne correspond pas (mauvais numéro ou mauvais code), ignoré")
                continue
            
            official_text = article_data.get("texte", "Texte non trouvé")
            article_num_found = article_data.get("num", "")
            
            analysis_task.append({
                "citation": cit['full_match'],
                "article_num_searched": cit['article_num'],
                "article_num_found": article_num_found,
                "user_draft_paragraph": cit['context'],
                "official_law_text": official_text
            })
        except Exception as e:
            print(f"Erreur pour {cit['full_match']}: {e}")

    # 3. Sauvegarde pour analyse par l'IA (Cascade)
    if analysis_task:
        output_file = "to_analyze.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(analysis_task, f, indent=2, ensure_ascii=False)
        print(f"\n✅ Données récupérées avec succès !")
        print(f"📄 Fichier généré : {output_file}")
        print("\n👉 Prochaine étape :")
        print("Demande-moi : 'Analyse le fichier to_analyze.json avec le protocole Strict RAG'.")
    else:
        print("Aucune donnée n'a pu être récupérée.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Usage: python legal_checker.py path/to/draft.md")
