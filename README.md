[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Ne-VwN1E)
# TP2 – Simulateur de Station Spatiale ORBIT-X 🛰️

⏰ **Date de remise** : Dimanche 22 février 2026 à 23h59

:mailbox_with_mail: **Remise** : sur Github Classrooms

---
## Objectif pédagogique

Ce travail pratique (TP2) vise à consolider **les notions Python vues au cours**.

Vous allez notamment pratiquer :
- Conditions (`if / elif / else`)
- Boucles (`for`, `while`)
- Structures de données (`list`, `dict`, `tuple`)
- Parcours et agrégation de données
- Algorithmes simples (tri, recherche, moyennes, comptages)

---
## Mise en contexte

La station spatiale **ORBIT-X** fonctionne en autonomie.
Un logiciel interne aide à :
- surveiller les modules,
- prioriser les interventions,
- gérer les ressources vitales,
- attribuer des équipements,
- analyser des rapports d’incidents.

Chaque exercice correspond à une brique de ce système.

---
## Structure du TP

```
exercice1.py  → Analyse des modules
exercice2.py  → Priorisation des interventions
exercice3.py  → Gestion des ressources vitales
exercice4.py  → Gestion d’équipements techniques
exercice5.py  → Analyse de rapports d’incidents
```

⚠️ **Consigne essentielle** :
Vous devez modifier **UNIQUEMENT** les sections marquées `# TODO`.

## 🚨 Erreurs courantes à éviter

### KeyError lors de l’accès aux dictionnaires
**Problème** : `KeyError` lorsqu’une clé attendue n’existe pas dans un dictionnaire  
(ex. : intervention sans champ `urgence`, ressource absente, module inconnu).

**Solution** :
```python
# Au lieu de :
urgence = intervention["urgence"]

# Utilisez :
urgence = intervention.get("urgence", 0)
```

Autre exemple (ressources) :
```python
consommation = besoins.get("oxygene", 0)
```

---

### Division par zéro
**Problème** : `ZeroDivisionError` lors du calcul de ratios ou de moyennes.

**Solution** :
```python
if temps_intervention > 0:
    ratio = criticite / temps_intervention
```
---

### Modification involontaire des structures d’entrée
**Problème** : modifier directement une liste ou un dictionnaire passé en paramètre,
ce qui fausse les tests suivants.

**Solution** :
```python
# Copie d’un dictionnaire
nouvelles_ressources = ressources.copy()
```

```python
# Copie d’une grille 2D
nouvelle_salle = [ligne.copy() for ligne in salle]
```

---

### IndexError avec les listes ou grilles
**Problème** : accès à un index inexistant dans une liste ou une grille 2D.

**Solution** :
```python
if 0 <= ligne < len(salle) and 0 <= colonne < len(salle[0]):
    case = salle[ligne][colonne]
```

---
# Exercice 1 – Analyse des modules de la station (3 points)

La station spatiale ORBIT-X est composée de plusieurs **modules techniques** (laboratoires, habitats, systèmes de contrôle, etc.).  
Chaque module nécessite des opérations de maintenance régulières, dont le coût, la durée et la criticité peuvent varier.

Dans cet exercice, vous devez analyser ces modules afin d’aider à la prise de décision.

---

## Représentation des données

Les modules sont représentés par un dictionnaire de la forme :
```python
modules = {
    "ModuleA": (cout_maintenance, temps_intervention, criticite),
    "ModuleB": (cout_maintenance, temps_intervention, criticite),
}
```

- `cout_maintenance` : coût d’une intervention (entier ≥ 0)
- `temps_intervention` : durée de l’intervention (entier ≥ 0)
- `criticite` : niveau de criticité du module (entier ≥ 0)

---

### Fonctions à compléter

#### 1️⃣ `analyser_modules(modules)`
- gérer le cas d’un dictionnaire vide,
- ignorer les modules dont `temps_intervention == 0`,
- trouver le module ayant le **meilleur ratio** `criticite / temps_intervention`,
- calculer le **coût moyen** et le **temps moyen**.

---
#### 2️⃣ `regrouper_modules_par_type(modules, types)`
- regrouper les modules par type,
- créer les listes si nécessaires,
- ignorer les modules sans type.

---
#### 3️⃣ `calculer_cout_total(modules, interventions)`
- calculer le coût total des maintenances prévues,
- ignorer les modules inexistants.

---
# Exercice 2 – Priorisation des interventions (4 points)

La station ORBIT-X reçoit régulièrement des **demandes d’intervention** pour assurer la maintenance et la sécurité de ses systèmes.
Ces interventions doivent être **priorisées** afin d’être traitées dans le bon ordre.

Dans cet exercice, vous allez manipuler des listes de dictionnaires représentant des interventions.

---

## Représentation des données

Chaque intervention est représentée par un dictionnaire contenant les clés suivantes :

```python
intervention = {
    "id": identifiant,
    "urgence": niveau_urgence,
    "duree": duree_estimee,
    "critique": True ou False
}
```

- `id` : identifiant unique de l’intervention
- `urgence` : niveau d’urgence (entier ≥ 0)
- `duree` : durée estimée (entier ≥ 0)
- `critique` : indique si l’intervention est critique (`True` ou `False`)

Certains champs peuvent être absents dans les dictionnaires fournis.

---

### Fonctions à compléter

#### 1️⃣ `calculer_priorite(intervention)`
Formule :
```
priorité = urgence×2 + duree + critique×10
```
- champs manquants → valeur 0.

---
#### 2️⃣ `trier_interventions(liste_interventions)`
- trier par priorité décroissante,
- **interdiction d’utiliser `sorted()`**,
- le tri doit être **stable**.

---
#### 3️⃣ `estimer_temps_interventions(liste_triee)`
- 1 unité de durée = 4 minutes,
- calculer le temps total et moyen.

---
#### 4️⃣ `identifier_interventions_urgentes(liste, seuil)`
- retourner les `id` dont l’urgence dépasse strictement le seuil.

---
# Exercice 3 – Gestion des ressources vitales (4 points)

La station ORBIT-X doit gérer en permanence ses **ressources vitales** (oxygène, eau, énergie, etc.).  
Chaque ressource est associée à une quantité disponible, et chaque activité consomme une certaine quantité de ressources.

Les ressources sont représentées par un dictionnaire :
```python
ressources = {
    "oxygene": 120,
    "eau": 80,
    "energie": 200
}
```

Les consommations ou besoins sont également représentés par des dictionnaires.

### Fonctions à compléter

#### 1️⃣ `verifier_ressources(ressources, besoins)`
- Vérifier si toutes les ressources nécessaires sont disponibles en quantité suffisante
- Retourner :
  - `True` et une liste vide si tout est suffisant
  - `False` et la liste des ressources manquantes sinon

---
#### 2️⃣ `mettre_a_jour_ressources(ressources, besoins, cycles)`
- Mettre à jour les quantités de ressources après un certain nombre de cycles
- **Ne pas modifier le dictionnaire original**
- Retourner un **nouveau dictionnaire** mis à jour

---
#### 3️⃣ `generer_alertes_ressources(ressources, seuil)`
- Générer une alerte si une ressource est **strictement inférieure** au seuil
- Pour chaque alerte, retourner :
  - la quantité actuelle
  - la quantité à commander pour atteindre 200 unités

---
#### 4️⃣ `calculer_cycles_possibles(ressources, consommations)`
- Calculer le nombre maximum de cycles possibles pour chaque activité
- Si une consommation est égale à 0, retourner 0 cycle
- Utiliser la **division entière**

---
#### 5️⃣ `optimiser_reapprovisionnement(ressources, objectifs, budget)`
- Acheter des ressources pour se rapprocher des objectifs
- Le coût est proportionnel à la quantité achetée
- Respecter strictement le budget
- Prioriser les ressources avec le **manque le plus important**

---
# Exercice 4 – Gestion d’équipements techniques (4 points)

La station ORBIT-X dispose d’une **salle d’équipements techniques** organisée sous forme de **grille 2D**.
Chaque case de la grille correspond à une zone pouvant contenir un équipement ou être inutilisable.

Les équipements peuvent accueillir **2 ou 4 personnes** et peuvent être dans différents états.

## Représentation de la salle

Chaque case de la grille contient une chaîne de caractères parmi :

- `X` : zone sans équipement
- `D2`, `D4` : équipement **disponible** (capacité 2 ou 4)
- `U2`, `U4` : équipement **utilisé**
- `M2`, `M4` : équipement **en maintenance**

Exemple de grille :
```python
[
    ["D2", "X",  "D4"],
    ["U2", "M4", "X"],
    ["X",  "D2", "U4"]
]
```

---

## Fonctions à compléter

### 1️⃣ `initialiser_salle(nb_rangees, nb_colonnes, positions)`

Vous devez :
- créer une grille de taille `nb_rangees × nb_colonnes`,
- initialiser toutes les cases à `"X"`,
- placer les équipements indiqués dans `positions`.

Chaque élément de `positions` est un tuple :
```python
(ligne, colonne, capacite)
```
où `capacite` vaut `2` ou `4`.

Les équipements placés sont **toujours disponibles** (`"D2"` ou `"D4"`).

---

### 2️⃣ `affecter_equipement(salle, position)`

- transformer un équipement **disponible** (`D2` ou `D4`) en équipement **utilisé** (`U2` ou `U4`),
- travailler sur une **copie de la grille** (ne jamais modifier la grille originale),
- si la case ne contient pas un équipement disponible, la grille est retournée inchangée.

---

### 3️⃣ `calculer_score_equipement(position, capacite, taille_equipe, bonus_supervision)`

Cette fonction calcule un **score d’attractivité** pour un équipement.

Règles :
- si `capacite < taille_equipe` → retourner `-1`,
- score de base : `100`,
- malus : `-10` par place inutilisée,
- bonus :
  - `+20` si l’équipement est sur un **bord de la salle**,
  - `+bonus_supervision` si l’équipement est sur la **première ligne**.

---

### 4️⃣ `trouver_meilleur_equipement(salle, taille_equipe)`

- parcourir toute la grille,
- identifier les équipements **disponibles** compatibles avec la taille de l’équipe,
- calculer leur score à l’aide de `calculer_score_equipement`,
- retourner un tuple :
```python
((ligne, colonne), capacite)
```

En cas d’égalité de score, **le premier équipement trouvé est conservé**.

Si aucun équipement n’est compatible, retourner `None`.

---

### 5️⃣ `generer_rapport_etat(salle)`

Vous devez produire un rapport sous forme de dictionnaire contenant :
- le nombre d’équipements disponibles, utilisés et en maintenance,
- séparés par capacité (`2` et `4`),
- le **taux d’indisponibilité** :
```
(nombre d’équipements utilisés + en maintenance) / nombre total d’équipements
```

Si aucun équipement n’est présent dans la salle, le taux d’indisponibilité doit être `0.0`.

---
# Exercice 5 – Analyse de rapports d’incidents (5 points)

La station ORBIT-X génère régulièrement des **rapports d’incidents** sous forme de texte libre.
Ces rapports doivent être analysés automatiquement afin d’évaluer l’état global de la station et d’identifier les problèmes récurrents.

Chaque rapport est une **chaîne de caractères** contenant des mots-clés positifs ou négatifs.

---

## Mots-clés et scores

Les mots-clés sont associés à un score (positif ou négatif) à l’aide d’un dictionnaire, par exemple :
```python
mots_cles = {
    "stable": 2,
    "optimal": 3,
    "nominal": 1,
    "ok": 1,
    "erreur": -2,
    "panne": -3,
    "defaillant": -3,
    "retard": -1,
    "surchauffe": -2,
    "fuite": -3,
}
```

---

## Fonctions à compléter

### 1️⃣ `analyser_rapport(texte, mots_cles)`

Cette fonction analyse le contenu d’un rapport.

Vous devez :
- ignorer la casse (`"OK"`, `"ok"`, `"Ok"` sont équivalents),
- ignorer la ponctuation,
- compter **toutes les occurrences** des mots-clés,
- calculer un score à partir d’un score initial de **5**,
- borner le score final entre **0 et 10** (inclus).

La fonction retourne :
```python
(score, liste_mots_detectes)
```
où `liste_mots_detectes` ne contient chaque mot-clé **qu’une seule fois**.

---

### 2️⃣ `categoriser_rapports(rapports, mots_cles)`

- Appliquer `analyser_rapport` à chaque rapport,
- Classer les rapports selon leur score :
  - **positif** : score ≥ 7
  - **neutre** : 4 ≤ score ≤ 6
  - **négatif** : score ≤ 3

Retourner un dictionnaire :
```python
{
    "positifs": [(rapport, score), ...],
    "neutres":  [(rapport, score), ...],
    "negatifs": [(rapport, score), ...],
}
```

Si la liste des rapports est vide, toutes les listes doivent être vides.

---

### 3️⃣ `identifier_problemes(rapports_negatifs, mots_cles_negatifs)`

- `rapports_negatifs` peut contenir :
  - des chaînes de caractères,
  - ou des tuples `(rapport, score)`.
- Compter le nombre total d’occurrences de chaque mot-clé négatif.
- Retourner un dictionnaire `{mot: nombre_occurrences}`.

Si aucun rapport n’est fourni, retourner un dictionnaire avec toutes les clés à `0`.

---

### 4️⃣ `generer_rapport_global(categories, problemes)`

Cette fonction génère un **bilan global**.

Vous devez calculer :
- `nb_positifs`, `nb_neutres`, `nb_negatifs`,
- `score_moyen` de **tous** les rapports,
- `top_problemes` : les **3 problèmes les plus fréquents**.

⚠️ Cas limite important :
- S’il n’y a **aucun rapport**, alors :
  - `score_moyen = 0.0`
  - `top_problemes = []`

---

### 5️⃣ `calculer_tendance(scores)`

Cette fonction analyse l’évolution des scores dans le temps.

- Si la liste est vide ou contient un seul élément → `"stable"`
- Séparer la liste en deux moitiés :
  - première moitié
  - seconde moitié (la plus grande si impair)
- Comparer les moyennes :
  - seconde > première → `"amelioration"`
  - seconde < première → `"degradation"`
  - égalité → `"stable"`

---
## Barème

| **Exercice** | **Fonction** | **Points** |
|-------------|--------------|------------|
| **EXERCICE 1 : Analyse des modules** | | **/3** |
| | `analyser_modules` | 1.5 |
| | `regrouper_modules_par_type` | 0.75 |
| | `calculer_cout_total` | 0.75 |
| **EXERCICE 2 : Priorisation des interventions** | | **/4** |
| | `calculer_priorite` | 0.75 |
| | `trier_interventions` | 1.75 |
| | `estimer_temps_interventions` | 0.75 |
| | `identifier_interventions_urgentes` | 0.75 |
| **EXERCICE 3 : Gestion des ressources vitales** | | **/4** |
| | `verifier_ressources` | 0.5 |
| | `mettre_a_jour_ressources` | 0.5 |
| | `generer_alertes_ressources` | 0.5 |
| | `calculer_cycles_possibles` | 1 |
| | `optimiser_reapprovisionnement` | 1.5 |
| **EXERCICE 4 : Gestion d’équipements techniques** | | **/4** |
| | `initialiser_salle` | 0.75 |
| | `affecter_equipement` | 0.75 |
| | `calculer_score_equipement` | 0.75 |
| | `trouver_meilleur_equipement` | 1 |
| | `generer_rapport_etat` | 0.75 |
| **EXERCICE 5 : Analyse de rapports d’incidents** | | **/5** |
| | `analyser_rapport` | 1.5 |
| | `categoriser_rapports` | 0.75 |
| | `identifier_problemes` | 1 |
| | `generer_rapport_global` | 1 |
| | `calculer_tendance` | 0.75 |
| **Total** | | **/20** |


---


