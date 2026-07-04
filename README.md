# Legal Anti-Hallucination Checker (RAPO)

Cette application permet de vérifier la véracité des citations juridiques dans un document (type RAPO) en interrogeant directement l'API officielle de Légifrance (PISTE).

## 🚀 Fonctionnement

1. **Extraction** : Le script utilise des expressions régulières pour identifier les citations (ex: "article L. 256-4 du Code de la Sécurité Sociale").
2. **Consultation** : Il interroge l'API Légifrance pour récupérer le texte officiel en vigueur.
3. **Préparation** : Il génère un fichier `to_analyze.json` contenant le texte original et le texte officiel côte à côte.
4. **Audit** : Ce fichier est ensuite analysé (via LLM ou manuellement) pour détecter les hallucinations.

## 🛠 Installation

1. Clonez le dépôt.
2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
3. Configurez vos accès PISTE dans un fichier `.env` :
   ```text
   PISTE_CLIENT_ID=votre_id
   PISTE_CLIENT_SECRET=votre_secret
   ```

## 📋 Utilisation

Lancez l'analyse sur un fichier Markdown :
```bash
python legal_checker.py votre_fichier.md
```

## 📂 Structure du projet

- `legal_checker.py` : Script principal.
- `to_analyze.json` : Données extraites pour audit.
- `.env` : Configuration (ignoré par Git).
- `requirements.txt` : Dépendances Python.

---
*Développé pour l'analyse de conformité juridique et la lutte contre les hallucinations des LLM.*
