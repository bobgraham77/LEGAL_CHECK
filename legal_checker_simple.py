import re
import json
from legal_checker import LegalParser

def main(input_md_path):
    with open(input_md_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extraction des citations
    print("Extraction des citations juridiques...")
    citations = LegalParser.extract_citations(content)
    print(f"Trouvé {len(citations)} citations.")
    
    # Génération du fichier pour analyse manuelle
    analysis_task = []
    for cit in citations:
        analysis_task.append({
            "citation": cit['full_match'],
            "article_num": cit['article_num'],
            "code_name": cit['code_name'],
            "user_draft_paragraph": cit['context'],
            "note": "Texte officiel non récupéré - Analyse basée sur connaissance juridique avec avertissement"
        })
    
    output_file = "to_analyze_manual.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(analysis_task, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Fichier généré : {output_file}")
    print(f"📊 {len(analysis_task)} citations extraites")
    print("\n👉 Prochaine étape :")
    print("Demande-moi : 'Analyse le fichier to_analyze_manual.json en mode strict avec avertissement'")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Usage: python legal_checker_simple.py RAPO_V2.md")
