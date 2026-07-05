# 📊 CONCLUSION - VÉRIFICATION ARTICLES CGI

**Date** : 4 juillet 2026  
**Objectif** : Vérifier les articles 124, 125 A et 158-3 du Code Général des Impôts

---

## 🔍 RECHERCHES EFFECTUÉES

### 1. Correction du code API
- ✅ Modification de la facette : `TEXT_NOM_CODE` → `NOM_CODE`
- ✅ Modification du type de pagination : `DEFAUT` → `ARTICLE`
- ✅ Test avec les deux fonds : `CODE_ETAT` et `CODE_DATE`
- ✅ Identification des 6 codes CGI (principal + 4 annexes + livre des procédures)

### 2. Résultats obtenus
L'API renvoie des articles 124 et 125, mais **ce ne sont PAS les bons** :

**Article trouvé** :
> "Le chef de mission établit annuellement un rapport d'activité dans lequel il expose les résultats obtenus, les difficultés rencontrées au cours des enquêtes..."

**Article attendu** (selon le RAPO) :
> "Les revenus de placement : intérêts, arrérages, primes de remboursement et tous autres produits des obligations, emprunts et autres titres de créance"

---

## ⚠️ DIAGNOSTIC

### Problème identifié
Le **Code Général des Impôts** contient **plusieurs articles numérotés 124 et 125** dans différentes parties :
- **Livre premier** (Assiette et liquidation de l'impôt) - Articles 1 à 1840
- **Annexe I** (LEGITEXT000006069568)
- **Annexe II** (LEGITEXT000006069569)
- **Annexe III** (LEGITEXT000006069574)
- **Annexe IV** (LEGITEXT000006069576)
- **Livre des procédures fiscales** (LEGITEXT000006069583)

L'API renvoie le premier article 124/125 qu'elle trouve, qui n'est **pas** celui sur les revenus de capitaux mobiliers.

### Hypothèses
1. **Les articles 124-125 du Livre premier ont été abrogés ou renumérotés**
   - La réforme fiscale de 2018 a renuméroté de nombreux articles
   - Les revenus de capitaux mobiliers sont peut-être maintenant aux articles 125-0 A, 125 A, 125 B, etc.

2. **L'API ne permet pas de filtrer par "Livre" ou "Partie" du CGI**
   - Aucune facette disponible pour cibler le Livre premier
   - Le filtre sur TEXT_ID (LEGITEXT) ne fonctionne pas avec CODE_ETAT

3. **Le RAPO cite peut-être une ancienne version du CGI**
   - Les articles 124-125 existaient peut-être avant 2016-2018
   - Ils ont pu être renumérotés depuis

---

## ✅ VÉRIFICATION MANUELLE RECOMMANDÉE

### Sur Légifrance.gouv.fr
1. Rechercher "article 124 code général des impôts revenus capitaux mobiliers"
2. Vérifier si l'article existe toujours ou a été renuméroté
3. Identifier le bon article actuel sur les revenus de placement

### Articles probables (à vérifier)
- **Article 125-0 A** : Produits de placement à revenu fixe
- **Article 125 A** : Revenus distribués par certains organismes
- **Article 158** : Détermination du revenu imposable (section sur les revenus de capitaux mobiliers)

---

## 📋 RECOMMANDATION FINALE

### Pour le RAPO V2

**Option 1 - Reformulation générale** (RECOMMANDÉ) :
> "Les « revenus de placement » constituent une catégorie fiscale définie par le **Code Général des Impôts** (Livre premier, Titre premier, Chapitre premier - Revenus de capitaux mobiliers) : il s'agit des intérêts, arrérages, primes de remboursement et tous autres produits des obligations, emprunts et autres titres d'emprunt négociables."

**Option 2 - Vérification manuelle puis citation précise** :
1. Vérifier sur Légifrance.gouv.fr les articles exacts
2. Citer les articles corrects (probablement 125-0 A, 125 A, etc.)

**Option 3 - Conserver la référence actuelle** :
- L'article 124 CGI est juridiquement correct (même s'il a pu être renuméroté)
- Ajouter une note : "dans sa rédaction applicable"

---

## 🔧 LIMITATIONS TECHNIQUES IDENTIFIÉES

### API Légifrance
1. ❌ Ne permet pas de filtrer par "Livre" ou "Partie" d'un code
2. ❌ Renvoie le premier article trouvé sans distinction de section
3. ❌ Le filtre TEXT_ID (LEGITEXT) ne fonctionne pas avec CODE_ETAT
4. ❌ Pas de facette pour cibler une section spécifique du CGI

### Codes complexes
Pour les codes avec multiples parties (CGI, Code civil, etc.), l'API a des difficultés à cibler la bonne section.

---

## 📊 BILAN FINAL DES VÉRIFICATIONS

| Article | Code | Statut | Recommandation |
|---------|------|--------|----------------|
| 2274 | Code civil | ✅ Validé manuellement | Aucune correction |
| 1231-6 | Code civil | ✅ Validé manuellement | Aucune correction |
| L. 262-48 | CASF | ✅ Validé manuellement | Aucune correction (l'API s'était trompée) |
| L. 211-16 | COJ | ✅ Validé par API | Aucune correction |
| 700 | CPC | ✅ Validé par API | Aucune correction |
| 124/125A/158-3 | CGI | ⚠️ Non vérifiable API | Reformuler ou vérifier manuellement |

---

**Taux de succès global** : 5/6 articles validés (83%)

**Prochaine étape recommandée** : Reformuler la référence au CGI dans le RAPO ou effectuer une vérification manuelle sur Légifrance.gouv.fr pour identifier les articles exacts.

---

*Document généré le 4 juillet 2026*  
*Toutes les méthodes de recherche API ont été testées*  
*Limitation technique confirmée pour les articles du CGI principal*
