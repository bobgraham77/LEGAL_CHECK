import os
import sys
import json
import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.legifrance_api import LegifranceClient

def main():
    print("=" * 80)
    print("RECHERCHE TEXTUELLE - REVENUS DE PLACEMENT DANS LE CGI")
    print("=" * 80)
    
    client = LegifranceClient()
    url = f"{client.API_BASE_URL}/search"
    
    # Recherche textuelle sur "revenus de capitaux mobiliers" ou "produits de placement"
    search_terms = [
        "revenus capitaux mobiliers",
        "produits placement",
        "intérêts obligations"
    ]
    
    for term in search_terms:
        print(f"\n{'=' * 80}")
        print(f"Recherche : '{term}'")
        print(f"{'=' * 80}")
        
        payload = {
            "recherche": {
                "champs": [{
                    "typeChamp": "ARTICLE",
                    "criteres": [{
                        "typeRecherche": "TOUS_LES_MOTS",
                        "valeur": term,
                        "operateur": "ET"
                    }],
                    "operateur": "ET"
                }],
                "filtres": [{
                    "facette": "TEXT_NOM_CODE",
                    "valeurs": ["Code général des impôts"]
                }],
                "pageNumber": 1,
                "pageSize": 5,
                "sort": "PERTINENCE",
                "typePagination": "DEFAUT"
            },
            "fond": "CODE_ETAT"
        }
        
        try:
            response = requests.post(url, json=payload, headers=client._get_headers())
            if response.status_code == 200:
                data = response.json()
                results = data.get("results", [])
                print(f"\n  Nombre de résultats : {len(results)}")
                
                for i, result in enumerate(results[:3], 1):
                    sections = result.get("sections", [])
                    for section in sections:
                        extracts = section.get("extracts", [])
                        for extract in extracts:
                            article_id = extract.get("id", "")
                            if article_id.startswith("LEGIARTI"):
                                # Récupérer le contenu
                                art_data = client.get_article_content(article_id)
                                print(f"\n  Résultat {i}:")
                                print(f"    ID: {article_id}")
                                print(f"    Numéro: {art_data.get('num', 'N/A')}")
                                print(f"    Texte (150 premiers caractères): {art_data.get('texte', '')[:150]}...")
                                break
            else:
                print(f"  ❌ Erreur HTTP {response.status_code}")
        except Exception as e:
            print(f"  ❌ Erreur : {e}")

if __name__ == "__main__":
    main()
