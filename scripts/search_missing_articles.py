import os
import sys
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.legifrance_api import LegifranceClient

def search_article_variants(client, article_num, code_name_variants):
    """Recherche un article avec plusieurs variantes du nom de code."""
    print(f"\n🔍 Recherche de l'article {article_num}...")
    
    for variant in code_name_variants:
        print(f"  Tentative avec : '{variant}'")
        try:
            art_id = client.search_article(article_num, variant)
            if art_id:
                article_data = client.get_article_content(art_id)
                print(f"  ✅ TROUVÉ avec '{variant}'")
                print(f"     ID: {art_id}")
                print(f"     Numéro: {article_data.get('num')}")
                print(f"     Code: {article_data.get('code')}")
                print(f"     Texte (100 premiers caractères): {article_data.get('texte', '')[:100]}...")
                return {
                    "article_num": article_num,
                    "code_variant_used": variant,
                    "article_id": art_id,
                    "article_num_found": article_data.get('num'),
                    "code_found": article_data.get('code'),
                    "texte": article_data.get('texte')
                }
        except Exception as e:
            print(f"  ❌ Erreur avec '{variant}': {e}")
    
    print(f"  ⚠️ Article {article_num} non trouvé avec aucune variante")
    return None

def main():
    print("=" * 80)
    print("RECHERCHE COMPLÉMENTAIRE - ARTICLES MANQUANTS")
    print("=" * 80)
    
    client = LegifranceClient()
    results = []
    
    # 1. Article L. 262-47 CASF (insaisissabilité RSA)
    print("\n" + "=" * 80)
    print("1. RECHERCHE : Article L. 262-47 CASF (insaisissabilité RSA)")
    print("=" * 80)
    result = search_article_variants(client, "L. 262-47", [
        "Code de l'action sociale et des familles",
        "Code de l'Action Sociale et des Familles",
        "CASF"
    ])
    if result:
        results.append(result)
    
    # 2. Article 125 CGI (revenus de placement)
    print("\n" + "=" * 80)
    print("2. RECHERCHE : Article 125 CGI (revenus de placement)")
    print("=" * 80)
    result = search_article_variants(client, "125", [
        "Code général des impôts",
        "Code Général des Impôts",
        "CGI"
    ])
    if result:
        results.append(result)
    
    # 3. Article L. 211-16 COJ
    print("\n" + "=" * 80)
    print("3. RECHERCHE : Article L. 211-16 COJ")
    print("=" * 80)
    result = search_article_variants(client, "L. 211-16", [
        "Code de l'organisation judiciaire",
        "Code de l'Organisation Judiciaire",
        "COJ"
    ])
    if result:
        results.append(result)
    
    # 4. Article 2274 Code civil
    print("\n" + "=" * 80)
    print("4. RECHERCHE : Article 2274 Code civil")
    print("=" * 80)
    result = search_article_variants(client, "2274", [
        "Code civil",
        "Code Civil",
        "CC"
    ])
    if result:
        results.append(result)
    
    # 5. Article 700 CPC
    print("\n" + "=" * 80)
    print("5. RECHERCHE : Article 700 CPC")
    print("=" * 80)
    result = search_article_variants(client, "700", [
        "Code de procédure civile",
        "Code de Procédure Civile",
        "CPC"
    ])
    if result:
        results.append(result)
    
    # 6. Article 1231-6 Code civil
    print("\n" + "=" * 80)
    print("6. RECHERCHE : Article 1231-6 Code civil")
    print("=" * 80)
    result = search_article_variants(client, "1231-6", [
        "Code civil",
        "Code Civil",
        "CC"
    ])
    if result:
        results.append(result)
    
    # Sauvegarde des résultats
    print("\n" + "=" * 80)
    print("RÉSULTATS")
    print("=" * 80)
    print(f"\n✅ {len(results)} article(s) trouvé(s) sur 6")
    
    if results:
        output_file = os.path.join("output", "articles_complements.json")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"📄 Résultats sauvegardés dans : {output_file}")
    else:
        print("⚠️ Aucun article trouvé")

if __name__ == "__main__":
    main()
