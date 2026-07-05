import os
import sys
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.legifrance_api import LegifranceClient

def main():
    print("=" * 80)
    print("LISTE DES CODES CONTENANT 'IMPÔTS'")
    print("=" * 80)
    
    client = LegifranceClient()
    
    url = f"{client.API_BASE_URL}/list/code"
    payload = {
        "pageNumber": 1,
        "pageSize": 200,
        "states": ["VIGUEUR"]
    }
    
    try:
        response = client._get_headers()
        import requests
        response = requests.post(url, json=payload, headers=client._get_headers())
        if response.status_code == 200:
            codes = response.json().get("results", [])
            
            print(f"\nNombre total de codes : {len(codes)}\n")
            
            # Filtrer les codes contenant "impôt" ou "fiscal"
            cgi_codes = []
            for code in codes:
                titre = code.get("titre", "")
                if "impôt" in titre.lower() or "fiscal" in titre.lower():
                    cgi_codes.append(code)
                    print(f"Titre : {titre}")
                    print(f"  CID : {code.get('cid', 'N/A')}")
                    print(f"  LEGITEXT : {code.get('id', 'N/A')}")
                    print(f"  Nature : {code.get('nature', 'N/A')}")
                    print()
            
            # Sauvegarder les résultats
            output_file = os.path.join("output", "cgi_codes_list.json")
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(cgi_codes, f, indent=2, ensure_ascii=False)
            print(f"📄 Résultats sauvegardés dans : {output_file}")
            
    except Exception as e:
        print(f"❌ Erreur : {e}")

if __name__ == "__main__":
    main()
