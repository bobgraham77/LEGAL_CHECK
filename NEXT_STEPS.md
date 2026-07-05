# 🎯 PROCHAINES ÉTAPES - CORRECTION DU RAPO V2

**Date** : 4 juillet 2026  
**Statut actuel** : Vérifications terminées ✅

---

## 📊 RÉSUMÉ DE LA SITUATION

### ✅ Ce qui a été fait
- Vérification complète de 6 articles via API Légifrance + vérifications manuelles
- Identification de 1 erreur majeure (article 124 CGI)
- Confirmation de 3 hallucinations (R. 142-1, L. 553-1, R. 132-1)
- Validation de 5 articles corrects

### ⏳ Ce qui reste à faire
- **Appliquer les corrections au RAPO_V2.md**
- Valider le RAPO corrigé
- Commit Git avec message approprié

---

## 🔴 CORRECTION URGENTE - Article 124 CGI

### Localisation
**Fichier** : `input/RAPO_V2.md`  
**Ligne** : 372

### Texte actuel (INCORRECT)
```
Or les « revenus de placement » constituent une catégorie fiscale précisément 
définie par l'article 124 du Code Général des Impôts : il s'agit des intérêts, 
arrérages, primes de remboursement et tous autres produits des obligations, 
emprunts et autres titres de créance.
```

### Texte corrigé (OPTION 1 - Recommandé)
```
Or les « revenus de placement » constituent une catégorie fiscale précisément 
définie par le Code Général des Impôts (articles 118 à 125-0 A) : il s'agit 
des produits de valeurs mobilières, intérêts d'obligations, dividendes et 
autres produits de placements financiers.
```

### Pourquoi c'est urgent
❌ **L'article 124 CGI EXCLUT les obligations** (inverse de ce que dit le RAPO)  
⚠️ La CAF peut retourner cette erreur contre vous  
✅ La correction renforce l'argumentation avec les bons articles

---

## 🟡 CORRECTIONS SECONDAIRES

### 1. Article R. 142-1 CSS (Hallucination confirmée)
**Action** : Retirer ou remplacer la référence  
**Raison** : L'article traite de la commission de recours, pas de l'opposabilité des délais

### 2. Article L. 553-1 CSS (Hallucination confirmée)
**Action** : Retirer ou remplacer la référence  
**Raison** : L'article traite de la prescription, pas du calcul du RSA

### 3. Article R. 132-1 CASF (Hallucination confirmée)
**Action** : Retirer ou remplacer la référence  
**Raison** : L'article traite des biens non productifs, pas de la définition des ressources

---

## 📋 COMMANDES À EXÉCUTER

### Option A - Correction manuelle
1. Ouvrir `input/RAPO_V2.md`
2. Chercher "article 124 du Code Général des Impôts"
3. Remplacer par le texte corrigé
4. Sauvegarder

### Option B - Correction automatique (via script)
```bash
# À créer si besoin
python scripts/apply_corrections.py
```

---

## 💾 COMMIT GIT RECOMMANDÉ

### Après correction
```bash
git add input/RAPO_V2.md
git commit -m "fix: correction article 124 CGI - remplacé par articles 118 à 125-0 A

L'article 124 CGI EXCLUT les obligations et titres d'emprunt négociables,
contrairement à ce qui était indiqué. Les bons articles pour les revenus
de placement sont les articles 118 à 125-0 A du CGI.

Vérification effectuée via API Légifrance et validation manuelle.
Voir RAPPORT_VERIFICATION_COMPLETE.md pour détails."

git push origin main
```

---

## 📁 FICHIERS GÉNÉRÉS

### Rapports de vérification
- ✅ `output/CORRECTIONS_DETAILLEES.md` - Analyse détaillée de chaque erreur
- ✅ `output/RESUME_RECHERCHE_COMPLEMENTAIRE.md` - Résumé des recherches
- ✅ `output/SYNTHESE_FINALE_VERIFICATION.md` - Synthèse des résultats
- ✅ `output/RAPPORT_VERIFICATION_COMPLETE.md` - Rapport exécutif complet
- ✅ `output/to_analyze.json` - Données brutes API

### Scripts créés
- ✅ `scripts/verify_cgi_articles.py` - Vérification articles CGI
- ✅ `scripts/list_cgi_codes.py` - Liste des codes CGI
- ✅ `scripts/search_missing_articles.py` - Recherche articles manquants

---

## ✅ CHECKLIST AVANT ENVOI DU RAPO

- [ ] Correction article 124 CGI appliquée
- [ ] Corrections hallucinations appliquées (R. 142-1, L. 553-1, R. 132-1)
- [ ] Relecture complète du RAPO
- [ ] Vérification cohérence argumentaire
- [ ] Commit Git effectué
- [ ] Backup créé
- [ ] RAPO prêt à envoyer

---

**Voulez-vous que j'applique automatiquement les corrections au RAPO_V2.md ?**
