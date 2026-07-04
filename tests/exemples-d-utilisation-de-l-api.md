![](media/image1.png){width="2.669815179352581in"
height="0.9431036745406824in"}

# Contenu {#contenu .list-paragraph}

[Utilisation de l'API Légifrance : Exemples de cas pratique
[1](#_Toc25768826)](#_Toc25768826)

[Contenu [1](#_Toc209017032)](#_Toc209017032)

[1. Connexion OAuth [3](#connexion-oauth)](#connexion-oauth)

[1.1. Obtention d'un jeton OAuth2.0 avec PISTE
[3](#obtention-dun-jeton-oauth2.0-avec-piste)](#obtention-dun-jeton-oauth2.0-avec-piste)

[1.2. Consommer l'API [3](#consommer-lapi)](#consommer-lapi)

[2. Récupérer un article en vigueur à une date donnée, d\'un code dont
on connaît l\'id
[4](#récupérer-un-article-en-vigueur-à-une-date-donnée-dun-code-dont-on-connaît-lid)](#récupérer-un-article-en-vigueur-à-une-date-donnée-dun-code-dont-on-connaît-lid)

[2.1. Étape 1 : Récupérer l'identifiant de l'article avec la méthode
POST /search
[4](#étape-1-récupérer-lidentifiant-de-larticle-avec-la-méthode-post-search)](#étape-1-récupérer-lidentifiant-de-larticle-avec-la-méthode-post-search)

[2.2. Étape 2 : Récupérer le contenu de l'article avec la méthode POST
/consult/getArticle
[4](#étape-2-récupérer-le-contenu-de-larticle-avec-la-méthode-post-consultgetarticle)](#étape-2-récupérer-le-contenu-de-larticle-avec-la-méthode-post-consultgetarticle)

[3. Récupérer un article en vigueur à une date donnée, d\'un texte
numéroté
[5](#récupérer-un-article-en-vigueur-à-une-date-donnée-dun-texte-numéroté)](#récupérer-un-article-en-vigueur-à-une-date-donnée-dun-texte-numéroté)

[3.1. Étape 1 : Trouver l'ordonnance avec la méthode POST /search
[5](#étape-1-trouver-lordonnance-avec-la-méthode-post-search)](#étape-1-trouver-lordonnance-avec-la-méthode-post-search)

[3.2. Étape 2 : trouver l'article de l'ordonnance avec la méthode POST
/search
[5](#étape-2-trouver-larticle-de-lordonnance-avec-la-méthode-post-search)](#étape-2-trouver-larticle-de-lordonnance-avec-la-méthode-post-search)

[3.3. Étape 3 : Récupérer le contenu de l'article avec la méthode POST
/consult/getArticle
[6](#étape-3-récupérer-le-contenu-de-larticle-avec-la-méthode-post-consultgetarticle)](#étape-3-récupérer-le-contenu-de-larticle-avec-la-méthode-post-consultgetarticle)

[4. Récupérer le texte complet d\'une loi promulguée dont on connaît le
n°
[7](#récupérer-le-texte-complet-dune-loi-promulguée-dont-on-connaît-le-n)](#récupérer-le-texte-complet-dune-loi-promulguée-dont-on-connaît-le-n)

[4.1. Étape 1 : Trouver l'identifiant de la loi avec la méthode POST
/search
[7](#étape-1-trouver-lidentifiant-de-la-loi-avec-la-méthode-post-search)](#étape-1-trouver-lidentifiant-de-la-loi-avec-la-méthode-post-search)

[4.2. Étape 2 : Récupérer le contenu de la loi avec la méthode POST
/consult/legiPart
[7](#étape-2-récupérer-le-contenu-de-la-loi-avec-la-méthode-post-consultlegipart)](#étape-2-récupérer-le-contenu-de-la-loi-avec-la-méthode-post-consultlegipart)

[5. Récupérer un article en vigueur à une date donnée, d\'une loi
identifiée par sa date de signature
[8](#récupérer-un-article-en-vigueur-à-une-date-donnée-dune-loi-identifiée-par-sa-date-de-signature)](#récupérer-un-article-en-vigueur-à-une-date-donnée-dune-loi-identifiée-par-sa-date-de-signature)

[5.1. Étape 1 : Trouver l'identifiant de la loi avec la méthode POST
/search
[8](#étape-1-trouver-lidentifiant-de-la-loi-avec-la-méthode-post-search-1)](#étape-1-trouver-lidentifiant-de-la-loi-avec-la-méthode-post-search-1)

[5.2. Étape2 : Une fois l'identifiant LEGIARTI récupéré, on l'utilise
avec la méthode /consult/getArticle
[8](#étape2-une-fois-lidentifiant-legiarti-récupéré-on-lutilise-avec-la-méthode-consultgetarticle)](#étape2-une-fois-lidentifiant-legiarti-récupéré-on-lutilise-avec-la-méthode-consultgetarticle)

[6. Récupérer un article en vigueur à une date donnée de la Constitution
ou à défaut le texte complet de la Constitution
[9](#récupérer-un-article-en-vigueur-à-une-date-donnée-de-la-constitution-ou-à-défaut-le-texte-complet-de-la-constitution)](#récupérer-un-article-en-vigueur-à-une-date-donnée-de-la-constitution-ou-à-défaut-le-texte-complet-de-la-constitution)

[6.1. Étape 1 : Trouver l'identifiant de l'article avec la méthode POST
/search
[9](#étape-1-trouver-lidentifiant-de-larticle-avec-la-méthode-post-search)](#étape-1-trouver-lidentifiant-de-larticle-avec-la-méthode-post-search)

[6.2. Étape 2 : Récupérer le contenu de l'article avec la méthode POST
/consult/getArticle
[10](#étape-2-récupérer-le-contenu-de-larticle-avec-la-méthode-post-consultgetarticle-1)](#étape-2-récupérer-le-contenu-de-larticle-avec-la-méthode-post-consultgetarticle-1)

[7. Recherche simple sur un mot dans un code
[10](#recherche-simple-sur-un-mot-dans-un-code)](#recherche-simple-sur-un-mot-dans-un-code)

[7.1. Exemple de requête par état juridique dans le fonds CODE
[10](#exemple-de-requête-par-état-juridique-dans-le-fonds-code)](#exemple-de-requête-par-état-juridique-dans-le-fonds-code)

[7.2. Exemple de requête par date de version ans le fonds CODE
[11](#exemple-de-requête-par-date-de-version-ans-le-fonds-code)](#exemple-de-requête-par-date-de-version-ans-le-fonds-code)

[8. Recherche d'une expression dans un code
[12](#recherche-dune-expression-dans-un-code)](#recherche-dune-expression-dans-un-code)

[9. Recherche croisée de mots dans les textes consolidés
[13](#recherche-croisée-de-mots-dans-les-textes-consolidés)](#recherche-croisée-de-mots-dans-les-textes-consolidés)

[10. Recherche dans la jurisprudence administrative
[13](#recherche-dans-la-jurisprudence-administrative)](#recherche-dans-la-jurisprudence-administrative)

[11. Recherche dans la jurisprudence judiciaire
[14](#recherche-dans-la-jurisprudence-judiciaire)](#recherche-dans-la-jurisprudence-judiciaire)

[11.1. Pour chercher tous les arrêts du mois de janvier 2025
[14](#pour-chercher-tous-les-arrêts-du-mois-de-janvier-2025)](#pour-chercher-tous-les-arrêts-du-mois-de-janvier-2025)

[11.2. Pour chercher par numéro d'affaire
[15](#pour-chercher-par-numéro-daffaire)](#pour-chercher-par-numéro-daffaire)

[12. Recherche dans les Journaux officiels
[15](#recherche-dans-les-journaux-officiels)](#recherche-dans-les-journaux-officiels)

[13. Recherche dans les conventions collectives
[16](#recherche-dans-les-conventions-collectives)](#recherche-dans-les-conventions-collectives)

[14. Récupération de contenu en masse
[17](#récupération-de-contenu-en-masse)](#récupération-de-contenu-en-masse)

**Historique des révisions**

  --------------------------------------------------------------------------
  Version    Date         Auteur    Modifications
  ---------- ------------ --------- ----------------------------------------
  V1         27/11/2019   DILA      Initialisation du document

  V2         26/07/2021   DILA      Mise à jour du document

  V3         17/09/2025   DILA      Mise à jour du document
  --------------------------------------------------------------------------

# Connexion OAuth

L'obtention d'un jeton OAuth par une application se fait via le
protocole OAuth2.0 avec le flux Client Credentials
(<https://tools.ietf.org/html/rfc6749#section-4.4>).

Des exemples supplémentaires de connexion OAuth (Python, Java,
JavaScript) sont disponibles sur le
[Gitlab](https://gitlab.com/piste_lab/oauth_connectors) de PISTE, après
inscription à Gitlab.

## [Obtention d'un jeton OAuth2.0 avec PISTE]{.underline}

La requête à effectuer est la suivante :

POST https://sandbox-oauth.piste.gouv.fr/api/oauth/token HTTP/1.1

Accept-Encoding: gzip,deflate

Content-Type: application/x-www-form-urlencoded

Content-Length: 140

Host: sandbox-oauth.piste.gouv.fr

Connection: Keep-Alive

User-Agent: Apache-HttpClient/4.1.1 (java 1.5)

grant_type=client_credentials&client_id=\<client_id_généré_sur_le_portail\>&client_secret=\<client_secret_généré_sur_le_portail\>&scope=openid

La réponse obtenue est la suivante :

{

\"access_token\":
\"th2uv3lq9zY2vAoth59QpYtCSID1iWn0AG6XhnjgAP54eoY1440vp3\",

\"token_type\": \"Bearer\",

\"expires_in\": 3600,

\"scope\": \"openid\"

}

La propriété \"access_token\" contient le jeton qui doit être envoyé à
chaque requête API.

La propriété \"expires_in\" correspond au délai d'expiration du jeton en
seconde.

## [Consommer l'API]{.underline}

Pour consommer l'API, il suffit d'ajouter l'entête \'Authorization:
Bearer \<access_token\>\' à chaque requête.

Par exemple :

curl -is -H \'Authorization: Bearer
ojECscMjYOh215MN6dUvAI3SOmhOa0nbg5R4tYvDWhZu5HB5ejMG74\' -X GET
https://sandbox-api.piste.gouv.fr/dila/legifrance/lf-engine-app/list/ping\'

Pour les requêtes de type POST, il faut ajouter également les entêtes

'accept: application/json' et 'Content-Type: application/json'.

# Récupérer un article en vigueur à une date donnée, d\'un code dont on connaît l\'id

**Exemple :**

-   **article L. 36-11 au 1er janvier 2018 du code LEGITEXT000006070987
    (postes et des communications électroniques)**

## [Étape 1]{.underline} : Récupérer l'identifiant de l'article avec la méthode POST /search

{

\"recherche\": {

\"champs\": \[

{

\"typeChamp\": \"NUM_ARTICLE\",

\"criteres\": \[

{

\"typeRecherche\": \"EXACTE\",

\"valeur\": \"L36-11\",

\"operateur\": \"ET\"

}

\],

\"operateur\": \"ET\"

}

\],

\"filtres\": \[

{

\"facette\": \"NOM_CODE\",

\"valeurs\": \[

\"Code des postes et des communications électroniques\"

\]

},

{

\"facette\": \"DATE_VERSION\",

\"singleDate\": 1514802418000

}

\],

\"pageNumber\": 1,

\"pageSize\": 10,

\"operateur\": \"ET\",

\"sort\": \"PERTINENCE\",

\"typePagination\": \"ARTICLE\"

},

\"fond\": \"CODE_DATE\"

}

## [Étape 2]{.underline} : Récupérer le contenu de l'article avec la méthode POST /consult/getArticle

{

\"id\": \"LEGIARTI000033219357\"

}

# Récupérer un article en vigueur à une date donnée, d\'un texte numéroté

**Exemples :**

-   **l'article 6 nonies au 1er janvier 2018 de l'ordonnance
    n°58-1100.**

-   **l'article 3-1 au 1er janvier 2018 de la loi n° 86-1067**

## [Étape 1]{.underline} : Trouver l'ordonnance avec la méthode POST /search

{

\"recherche\": {

\"champs\": \[

{

\"typeChamp\": \"NUM\",

\"criteres\": \[

{

\"typeRecherche\": \"EXACTE\",

\"valeur\": \"58-1100\",

\"operateur\": \"ET\"

}

\],

\"operateur\": \"ET\"

}

\],

\"filtres\": \[

{

\"facette\": \"DATE_VERSION\",

\"singleDate\": 1514802418000

}

\],

\"pageNumber\": 1,

\"pageSize\": 10,

\"operateur\": \"ET\",

\"sort\": \"PERTINENCE\",

\"typePagination\": \"DEFAUT\"

},

\"fond\": \"LODA_DATE\"

}

## [Étape 2]{.underline} : trouver l'article de l'ordonnance avec la méthode POST /search

{

\"recherche\": {

\"champs\": \[

{

\"typeChamp\": \"NUM\",

\"criteres\": \[

{

\"typeRecherche\": \"EXACTE\",

\"valeur\": \"58-1100\",

\"operateur\": \"ET\"

}

\],

\"operateur\": \"ET\"

},

{

\"typeChamp\": \"NUM_ARTICLE\",

\"criteres\": \[

{

\"typeRecherche\": \"EXACTE\",

\"valeur\": \"6 nonies\",

\"operateur\": \"ET\"

}

\],

\"operateur\": \"ET\"

}

\],

\"filtres\": \[

{

\"facette\": \"DATE_VERSION\",

\"singleDate\": 1514802418000

}

\],

\"pageNumber\": 1,

\"pageSize\": 10,

\"operateur\": \"ET\",

\"sort\": \"PERTINENCE\",

\"typePagination\": \"DEFAUT\"

},

\"fond\": \"LODA_DATE\"

}

## [Étape 3]{.underline} : Récupérer le contenu de l'article avec la méthode POST /consult/getArticle

{

\"id\": \"LEGIARTI000035937614\"

}

# Récupérer le texte complet d\'une loi promulguée dont on connaît le n°

**Exemple :**

-   **la loi n°2019-290 en vigueur à la date d\'aujourd\'hui**

## [Étape 1]{.underline} : Trouver l'identifiant de la loi avec la méthode POST /search

{

\"recherche\": {

\"champs\": \[

{

\"typeChamp\": \"NUM\",

\"criteres\": \[

{

\"typeRecherche\": \"EXACTE\",

\"valeur\": \"2019-290\",

\"operateur\": \"ET\"

}

\],

\"operateur\": \"ET\"

}

\],

\"filtres\": \[

{

\"facette\": \"DATE_VERSION\",

\"singleDate\": 1561132975000

},

{

\"facette\": \"TEXT_LEGAL_STATUS\",

\"valeur\": \"VIGUEUR\"

}

\],

\"pageNumber\": 1,

\"pageSize\": 10,

\"operateur\": \"ET\",

\"sort\": \"PERTINENCE\",

\"typePagination\": \"DEFAUT\"

},

\"fond\": \"LODA_ETAT\"

}

## [Étape 2]{.underline} : Récupérer le contenu de la loi avec la méthode POST /consult/legiPart

{

\"date\": 1561132975000,

\"textId\": \"LEGITEXT000038359719\"

}

# Récupérer un article en vigueur à une date donnée, d\'une loi identifiée par sa date de signature

**Exemples :**

-   **article 57 de la loi du 17 juillet 1978 en vigueur aujourd\'hui**

## [Étape 1]{.underline} : Trouver l'identifiant de la loi avec la méthode POST /search

{

\"recherche\": {

\"champs\": \[

{

\"typeChamp\": \"NUM_ARTICLE\",

\"criteres\": \[

{

\"typeRecherche\": \"EXACTE\",

\"valeur\": \"57\",

\"operateur\": \"ET\"

}

\],

\"operateur\": \"ET\"

}

\],

\"filtres\": \[

{

\"facette\": \"DATE_SIGNATURE\",

\"dates\":

{

\"start\": \"1978-07-17\",

\"end\": \"1978-07-17\"

}

},

{

\"facette\": \"DATE_VERSION\",

\"singleDate\": 1571664723166

},

{

\"facette\": \"TEXT_LEGAL_STATUS\",

\"valeur\": \"VIGUEUR\"

}

\],

\"pageNumber\": 1,

\"pageSize\": 1,

\"operateur\": \"ET\",

\"sort\": \"PERTINENCE\",

\"typePagination\": \"ARTICLE\"

},

\"fond\": \"LODA_DATE\"

}

## [Étape2 : Une fois l'identifiant LEGIARTI récupéré, on l'utilise avec la méthode /consult/getArticle]{.underline}

{

\"id\": \"LEGIARTI000006528277\"

}

# Récupérer un article en vigueur à une date donnée de la Constitution ou à défaut le texte complet de la Constitution

**Exemple :**

-   **article 54 de la Constitution**

## [Étape 1]{.underline} : Trouver l'identifiant de l'article avec la méthode POST /search

{

\"recherche\": {

\"champs\": \[

{

\"typeChamp\": \"TITLE\",

\"criteres\": \[

{

\"typeRecherche\": \"EXACTE\",

\"valeur\": \"Constitution\",

\"operateur\": \"ET\"

}

\],

\"operateur\": \"ET\"

},

{

\"typeChamp\": \"NUM_ARTICLE\",

\"criteres\": \[

{

\"typeRecherche\": \"EXACTE\",

\"valeur\": \"54\",

\"operateur\": \"ET\"

}

\],

\"operateur\": \"ET\"

}

\],

\"filtres\": \[

{

\"facette\": \"DATE_VERSION\",

\"singleDate\": 1561132975000

},

{

\"facette\": \"TEXT_LEGAL_STATUS\",

\"valeur\": \"VIGUEUR\"

}

\],

\"pageNumber\": 1,

\"pageSize\": 10,

\"operateur\": \"ET\",

\"sort\": \"PERTINENCE\",

\"typePagination\": \"DEFAUT\"

},

\"fond\": \"LODA_ETAT\"

}

## [Étape 2]{.underline} : Récupérer le contenu de l'article avec la méthode POST /consult/getArticle

{

\"id\": \"LEGIARTI000006527539\"

}

# Recherche simple sur un mot dans un code

Pour rechercher dans les codes, vous avez deux fonds disponibles selon
les besoins :

\- CODE_ETAT : recherche dans les codes par état juridique

\- CODE_DATE : recherche dans les codes par date de version

## Exemple de requête par état juridique dans le fonds CODE

{

\"fond\": \"CODE_ETAT\",

\"recherche\": {

\"champs\": \[{

\"typeChamp\": \"ARTICLE\",

\"criteres\": \[{

\"typeRecherche\": \"UN_DES_MOTS\",

\"valeur\": \"responsabilite\",

\"operateur\": \"ET\"

}

\],

\"operateur\": \"ET\"

}

\],

\"filtres\": \[{

\"facette\": \"TEXT_NOM_CODE\",

\"valeurs\": \[

\"Code civil\"

\]

}

\],

\"pageNumber\": 1,

\"pageSize\": 10,

\"operateur\": \"ET\",

\"sort\": \"PERTINENCE\",

\"typePagination\": \"DEFAUT\"

}

}

## Exemple de requête par date de version ans le fonds CODE

{

\"fond\": \"CODE_DATE\",

\"recherche\": {

\"champs\": \[

{

\"typeChamp\": \"ARTICLE\",

\"criteres\": \[

{

\"typeRecherche\": \"UN_DES_MOTS\",

\"valeur\": \"responsabilite\",

\"operateur\": \"ET\"

}

\],

\"operateur\": \"ET\"

}

\],

\"filtres\": \[

{

\"facette\": \"NOM_CODE\",

\"valeurs\": \[

\"Code civil\"

\]

},

{

\"facette\": \"DATE_VERSION\",

\"singleDate\": \"2025-04-15\"

}

\],

\"pageNumber\": 1,

\"pageSize\": 10,

\"operateur\": \"ET\",

\"sort\": \"PERTINENCE\",

\"typePagination\": \"DEFAUT\"

}

}

# Recherche d'une expression dans un code

La documentation Swagger précise les valeurs possibles pour
\"typeRecherche\" :

\[ UN_DES_MOTS, EXACTE, TOUS_LES_MOTS_DANS_UN_CHAMP, AUCUN_DES_MOTS,
AUCUNE_CORRESPONDANCE_A\_CETTE_EXPRESSION \]

Si vous recherchez une expression, vous pouvez indiquer \"UN_DES_MOTS\"
et préciser la proximité, c\'est-à-dire la distance maximale, en mots,
entre les termes recherchés.

Vous pouvez également sélectionner le type de recherche EXACTE.

Voici un exemple de requête complète par état juridique dans le fonds
CODE :

{

\"fond\": \"CODE_ETAT\",

\"recherche\": {

\"champs\": \[{

\"typeChamp\": \"ARTICLE\",

\"criteres\": \[{

\"typeRecherche\": \"UN_DES_MOTS\",

\"valeur\": \"outrage a agent\",

\"operateur\": \"ET\"

}

\],

\"operateur\": \"ET\"

}

\],

\"filtres\": \[{

\"facette\": \"TEXT_NOM_CODE\",

\"valeurs\": \[

\"Code pénal\"

\]

}

\],

\"pageNumber\": 1,

\"pageSize\": 10,

\"operateur\": \"ET\",

\"sort\": \"PERTINENCE\",

\"typePagination\": \"DEFAUT\"

}

}

# Recherche croisée de mots dans les textes consolidés

Pour effectuer une recherche croisée, il suffit de définir plusieurs
critères de recherche dans votre requête.

Voici un exemple de requête dans le fonds LODA_DATE :

{

\"fond\": \"LODA_DATE\",

\"recherche\": {

\"champs\": \[{

\"criteres\": \[{

\"criteres\": \[{

\"typeRecherche\": \"UN_DES_MOTS\",

\"valeur\": \"mineur\",

\"operateur\": \"ET\"

}

\],

\"operateur\": \"ET\",

\"proximite\": 2,

\"typeRecherche\": \"UN_DES_MOTS\",

\"valeur\": \"travail\"

}

\],

\"operateur\": \"ET\",

\"typeChamp\": \"ALL\"

}

\],

\"fromAdvancedRecherche\": false,

\"operateur\": \"ET\",

\"pageNumber\": 1,

\"pageSize\": 10,

\"secondSort\": \"ID\",

\"sort\": \"SIGNATURE_DATE_DESC\",

\"typePagination\": \"DEFAUT\"

}

}

# Recherche dans la jurisprudence administrative

Pour chercher tous les arrêts de type « CESEDA » sur une période
donnée :

{

\"fond\": \"CETAT\",

\"recherche\": {

\"champs\": \[

{

\"criteres\": \[

{

\"valeur\": \"CESEDA\",

\"proximite\": 2,

\"operateur\": \"ET\",

\"typeRecherche\": \"UN_DES_MOTS\"

}

\],

\"operateur\": \"ET\",

\"typeChamp\": \"ALL\"

}

\],

\"filtres\": \[

{

\"facette\": \"DATE_DECISION\",

\"dates\": {

\"start\": \"2000-01-01\",

\"end\": \"2005-01-01\"

}

}

\],

\"fromAdvancedRecherche\": false,

\"pageSize\": 100,

\"operateur\": \"ET\",

\"typePagination\": \"DEFAUT\",

\"pageNumber\": 1,

\"sort\": \"PERTINENCE\",

\"secondSort\": \"DATE_DESC\"

}

}

# Recherche dans la jurisprudence judiciaire

## Pour chercher tous les arrêts du mois de janvier 2025

{

\"fond\": \"JURI\",

\"recherche\": {

\"champs\": \[{

\"criteres\": \[{

\"operateur\": \"ET\",

\"proximite\": 2,

\"typeRecherche\": \"UN_DES_MOTS\",

\"valeur\": \"\*\"

}

\],

\"operateur\": \"ET\",

\"typeChamp\": \"ALL\"

}

\],

\"filtres\": \[{

\"facette\": \"CASSATION_NATURE_DECISION\",

\"valeurs\": \[

\"ARRET\"

\]

}, {

\"facette\": \"DATE_DECISION\",

\"dates\": {

\"start\": \"2025-01-01\",

\"end\": \"2025-01-31\"

}

}

\],

\"fromAdvancedRecherche\": false,

\"operateur\": \"ET\",

\"pageNumber\": 1,

\"pageSize\": 10,

\"secondSort\": \"DATE_DESC\",

\"sort\": \"PERTINENCE\",

\"typePagination\": \"DEFAUT\"

}

}

## Pour chercher par numéro d'affaire

{

\"fond\": \"JURI\",

\"recherche\": {

\"champs\": \[

{

\"criteres\": \[

{

\"operateur\": \"ET\",

\"typeRecherche\": \"EXACTE\",

\"valeur\": \"17/030701\"

}

\],

\"operateur\": \"ET\",

\"typeChamp\": \"NUM_AFFAIRE\"

}

\],

\"fromAdvancedRecherche\": false,

\"operateur\": \"ET\",

\"pageNumber\": 1,

\"pageSize\": 10,

\"secondSort\": \"ID\",

\"sort\": \"DATE_DESC\",

\"typePagination\": \"DEFAUT\"

}

}

# Recherche dans les Journaux officiels

Pour récupérer le contenu d'un Journal officiel, vous pouvez procéder de
la façon suivante :

Etape 1 :

Récupérer le JORFCONT (identifiant du conteneur d'un Journal officiel)
d'une publication d'un JO avec le point d'entrée /consult/lastNJo en
passant le nombre de JO que vous voulez récupérer :

{

\"nbElement\": 5

}

-   Ce chiffre doit être inférieur à 2500, sinon vous aurez des erreurs

Etape 2 :

Vous pouvez utiliser le point d'entrée /consult/jorfCont pour récupérer
les JORFTEXT (identifiant de chaque texte publié au JO) :

{

\"highlightActivated\": true,

\"id\": \"JORFCONT000022470431\",

\"pageNumber\": 1,

\"pageSize\": 10

}

-   Via ce point d'entrée vous pouvez aussi passer une période pour
    récupérer tous les JORFCONT pour une période donnée (cf. la
    documentation de l'API - swagger).

Etape 3 :

Vous pourrez appeler le point d'entrée /consult/jorf avec les JORFTEXT
récupérés à l'étape 2. Cela sera plus pertinent que d'utiliser le point
d'entrée getJoWithNor car tous les textes n'ont pas de NOR.

{

\"highlightActivated\": true,

\"id\": \"JORFCONT000022470431\",

\"pageNumber\": 1,

\"pageSize\": 10

}

A noter, les JO anciens ne comportent pas de version HTML des textes.
Vous ne pourrez donc pas les récupérer via l'API (avant juin 2004).

# Recherche dans les conventions collectives

Pour rechercher des mots-clés dans le titre des conventions
collectives :

{

\"fond\": \"KALI\",

\"recherche\": {

\"champs\": \[

{

\"typeChamp\": \"TITLE\",

\"operateur\": \"ET\",

\"criteres\": \[

{

\"valeur\": \"santé prévoyance\",

\"typeRecherche\": \"TOUS_LES_MOTS_DANS_UN_CHAMP\",

\"operateur\": \"ET\"

}

\]

}

\],

\"sort\": \"SIGNATURE_DATE_DESC\",

\"fromAdvancedRecherche\": \"False\",

\"pageNumber\": 1,

\"pageSize\": 25,

\"typePagination\": \"DEFAUT\",

\"secondSort\": \"PERTINENCE\",

\"operateur\": \"ET\"

}

}

Pour recherche sur le numéro IDCC :

{

\"fond\": \"KALI\",

\"recherche\": {

\"champs\": \[

{

\"typeChamp\": \"IDCC\",

\"operateur\": \"ET\",

\"criteres\": \[

{

\"valeur\": \"2098\",

\"typeRecherche\": \"TOUS_LES_MOTS_DANS_UN_CHAMP\",

\"operateur\": \"ET\"

}

\]

}

\],

\"sort\": \"PERTINENCE\",

\"fromAdvancedRecherche\": \"False\",

\"pageNumber\": 1,

\"pageSize\": 25,

\"typePagination\": \"DEFAUT\",

\"operateur\": \"ET\"

}

}

# Récupération de contenu en masse

[Alternativement à l'API,]{.underline} vous pouvez aussi utiliser l'open
data de Légifrance qui est proposé ici avec toutes nos ressources au
format XML :

<https://echanges.dila.gouv.fr/OPENDATA/>

Les différents freemium de chaque fonds permettent de récupérer l'état
du fonds à la date indiquée. Il faut ensuite récupérer les archives
suivantes dans l'ordre de la plus ancienne à la plus récente.

Les fonds de Légifrance sont : ACCO / BOCC / CAPP / CASS / CIRCULAIRES /
CNIL / CONSTIT / DOLE / Debats  / INCA / JADE / KALI / LEGI /
Questions-Reponses.

Vous aurez à chaque fois un document appelé « présentation » expliquant
les données que vous pouvez trouver sous chaque fonds. La DTD_LEGIFRANCE
vous permettra également de mieux comprendre la structuration des
données.
