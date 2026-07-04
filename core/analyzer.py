class ComplianceChecker:
    """Moteur de préparation pour analyse externe."""
    def __init__(self):
        pass
    
    def prepare_analysis(self, citations, legifrance_client):
        """Prépare les données pour l'analyse anti-hallucination."""
        analysis_task = []
        for cit in citations:
            print(f"Récupération de {cit['full_match']}...")
            try:
                art_id = legifrance_client.search_article(cit['article_num'], cit['code_name'])
                if not art_id:
                    print(f"  ❌ Article non trouvé sur Légifrance : {cit['article_num']}")
                    continue
                
                article_data = legifrance_client.get_article_content(art_id, cit['article_num'], cit['code_name'])
                if article_data.get("mismatch"):
                    print(f"  ⚠️ Article ne correspond pas (mauvais numéro ou mauvais code), ignoré")
                    continue
                
                analysis_task.append({
                    "citation": cit['full_match'],
                    "article_num_searched": cit['article_num'],
                    "article_num_found": article_data.get("num", ""),
                    "user_draft_paragraph": cit['context'],
                    "official_law_text": article_data.get("texte", "Texte non trouvé")
                })
            except Exception as e:
                print(f"  ❌ Erreur pour {cit['full_match']}: {e}")
        return analysis_task
