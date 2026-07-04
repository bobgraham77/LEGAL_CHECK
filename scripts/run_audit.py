import os
import sys
import json

# Ajouter le dossier parent au path pour importer core
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.legifrance_api import LegifranceClient
from core.parser import LegalParser
from core.analyzer import ComplianceChecker

def main(input_path):
    # Vérifier l'existence du fichier
    if not os.path.exists(input_path):
        print(f"Erreur : Le fichier {input_path} n'existe pas.")
        return

    # Créer le dossier output s'il n'existe pas
    os.makedirs("output", exist_ok=True)

    # 1. Lecture du fichier
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 2. Extraction
    print("Étape 1 : Extraction des citations...")
    parser = LegalParser()
    citations = parser.extract_citations(content)
    print(f"Trouvé {len(citations)} citations.")
    
    # 3. Récupération API
    print("Étape 2 : Consultation Légifrance...")
    legifrance = LegifranceClient()
    checker = ComplianceChecker()
    analysis_data = checker.prepare_analysis(citations, legifrance)
    
    # 4. Sauvegarde
    if analysis_data:
        output_file = os.path.join("output", "to_analyze.json")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(analysis_data, f, indent=2, ensure_ascii=False)
        print(f"\n✅ Données récupérées avec succès !")
        print(f"📄 Fichier généré : {output_file}")
    else:
        print("\n❌ Aucune donnée n'a pu être récupérée.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Usage: python scripts/run_audit.py input/votre_fichier.md")
