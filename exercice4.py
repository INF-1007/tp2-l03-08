"""
TP2 – Exercice 4 : Gestion d’équipements techniques (Centre ORBIT-X)

Contexte :
Le centre ORBIT-X possède une salle d’équipements techniques organisée en grille 2D.
Chaque case peut contenir un équipement (machine, banc de test, simulateur),
ou être inutilisable.

Chaque équipement a :
- une CAPACITÉ (2 ou 4 personnes)
- un ÉTAT :
    - Disponible
    - Utilisé
    - En maintenance

Codes utilisés dans la grille :
- 'X'  : zone sans équipement
- 'D2' : équipement DISPONIBLE, capacité 2
- 'D4' : équipement DISPONIBLE, capacité 4
- 'U2' : équipement UTILISÉ, capacité 2
- 'U4' : équipement UTILISÉ, capacité 4
- 'M2' : équipement en MAINTENANCE, capacité 2
- 'M4' : équipement en MAINTENANCE, capacité 4

Objectifs :
1) Initialiser la grille
2) Affecter un équipement disponible
3) Trouver le meilleur équipement pour une équipe
4) Générer un rapport d’état global
"""

# ------------------------------------------------------------------
# Fonction fournie – NE PAS MODIFIER
# ------------------------------------------------------------------

def afficher_salle(salle):
    print("\n=== Salle d’équipements ===")
    print("   ", end="")
    for j in range(len(salle[0])):
        print(f" {j}", end="")
    print()
    for i, rangee in enumerate(salle):
        print(f"{i}: ", end="")
        for case in rangee:
            print(f" {case}", end="")
        print()
    print("=" * 30)


# ------------------------------------------------------------------
# 1) Initialisation de la grille
# ------------------------------------------------------------------

def initialiser_salle(nb_rangees, nb_colonnes, positions_equipements):
    """
    Initialise la salle d’équipements.

    Args:
        nb_rangees (int)
        nb_colonnes (int)
        positions_equipements (list):
            liste de tuples (rangee, colonne, capacite)
            capacite = 2 ou 4

    Returns:
        list: grille 2D remplie de 'X', 'D2' ou 'D4'
    """
    salle = []

    # TODO 1 :
    # Créer une grille nb_rangees × nb_colonnes remplie de 'X'
    for i in range(nb_rangees):
        rangee = []
        for j in range(nb_colonnes):
            rangee.append('X')
        salle.append(rangee)

    # TODO 2 :
    # Pour chaque equipement (voir sa position) :
    #   - si capacite == 2, X -> 'D2'
    #   - si capacite == 4, X -> 'D4'
    for (r, c, capacite) in positions_equipements:
        if capacite == 2:
            salle[r][c] = 'D2'
        elif capacite == 4:
            salle[r][c] = 'D4'

    return salle


# -------------------------------------------------------------------
# 2) Affection des equipements
# -------------------------------------------------------------------


def affecter_equipement(salle, position):
    """
    Affecte un équipement DISPONIBLE.

    Args:
        salle (list): grille 2D
        position (tuple): (rangee, colonne)

    Returns:
        list: nouvelle grille (copie profonde)
            - 'D2' devient 'U2'
            - 'D4' devient 'U4'

    Règles :
    - Modifier uniquement si la case est 'D2' ou 'D4'
    - Sinon, ne rien faire
    """

    # TODO : Faire une copie de la salle et la nommer "nouvelle"
    nouvelle = []
    for rangee in salle:
        nouvelle.append(rangee[:])

    # TODO :
    # Pour la position donnée :
    #      si nouvelle[r][c] == 'D2' -> 'U2'
    #      si nouvelle[r][c] == 'D4' -> 'U4'
    r, c = position

    if nouvelle[r][c] == 'D2':
        nouvelle[r][c] = 'U2'
    elif nouvelle[r][c] == 'D4':
        nouvelle[r][c] = 'U4'

    return nouvelle


# -------------------------------------------------------------------
# 3) Calcul du score d'un equipement
# -------------------------------------------------------------------

def calculer_score_equipement(position, capacite, taille_equipe, nb_colonnes):
    """
    Calcule un score pour un équipement.

    Règles EXACTES :
    - Si capacite < taille_equipe : retourner -1
    - Base : 100 points
    - Pénalité : -10 par place inutilisée
        places_vides = capacite - taille_equipe
    - Bonus accès rapide : +20 si colonne == 0 ou colonne == nb_colonnes - 1
    - Bonus supervision : +5 si rangée < 3

    Args:
        position (tuple): (rangee, colonne)
        capacite (int): 2 ou 4
        taille_equipe (int)
        nb_colonnes (int)

    Returns:
        int: score ou -1
    """
    score = 0

    # TODO 1 : gérer le cas équipement trop petit
    if capacite < taille_equipe:
        return -1

    # TODO 2 : score de base
    score = 100

    # TODO 3 : pénalité gaspillage
    places_vides = capacite - taille_equipe
    score -= places_vides * 10

    # TODO 4 : bonus accès rapide
    r, c = position
    if c == 0 or c == nb_colonnes - 1:
        score += 20

    # TODO 5 : bonus supervision
    if r < 3:
        score += 5

    return score


# -------------------------------------------------------------------
# 4) Recherche du meilleur equipement
# -------------------------------------------------------------------


def trouver_meilleur_equipement(salle, taille_equipe):
    """
    Trouve le meilleur équipement DISPONIBLE pour une équipe.

    Args:
        salle (list): grille 2D
        taille_equipe (int)

    Returns:
        tuple ou None :
            - ((rangee, colonne), capacite)
            - None si aucun équipement compatible

    Règles :
    - Considérer uniquement 'D2' et 'D4'
    - Score maximal
    - En cas d’égalité, conserver le premier rencontré
    """
    meilleur = None
    meilleur_score = -1

    # TODO :
    # Parcourir la grille
    #   - si case == 'D2' ou 'D4'
    #       extraire capacite depuis la chaîne
    #       calculer le score
    #       comparer au meilleur

    nb_colonnes = len(salle[0])

    for i in range(len(salle)):
        for j in range(len(salle[i])):

            case = salle[i][j]

            if case == 'D2' or case == 'D4':

                capacite = int(case[1])
                score = calculer_score_equipement((i, j), capacite, taille_equipe, nb_colonnes)

                if score > meilleur_score:
                    meilleur_score = score
                    meilleur = ((i, j), capacite)

    return meilleur


# -------------------------------------------------------------------
# 5) Generation d'un rapport d'etat
# -------------------------------------------------------------------

def generer_rapport_etat(salle):
    """
    Génère un rapport global sur l’état des équipements.

    À compter :
    - disponibles 2 / 4
    - utilisés 2 / 4
    - maintenance 2 / 4

    Taux d’indisponibilité :
        (utilisés + maintenance) / total_equipements

    Returns:
        dict
    """
    rapport = {
        'disponibles_2': 0,
        'disponibles_4': 0,
        'utilises_2': 0,
        'utilises_4': 0,
        'maintenance_2': 0,
        'maintenance_4': 0,
        'taux_indisponibilite': 0.0
    }

    # TODO 1 : parcourir la grille et compter chaque type
    total_equipements = 0
    indisponibles = 0

    for rangee in salle:
        for case in rangee:

            if case == 'D2':
                rapport['disponibles_2'] += 1
                total_equipements += 1

            elif case == 'D4':
                rapport['disponibles_4'] += 1
                total_equipements += 1

            elif case == 'U2':
                rapport['utilises_2'] += 1
                total_equipements += 1
                indisponibles += 1

            elif case == 'U4':
                rapport['utilises_4'] += 1
                total_equipements += 1
                indisponibles += 1

            elif case == 'M2':
                rapport['maintenance_2'] += 1
                total_equipements += 1
                indisponibles += 1

            elif case == 'M4':
                rapport['maintenance_4'] += 1
                total_equipements += 1
                indisponibles += 1

    # TODO 2 : calculer le taux (gérer division par zéro)
    if total_equipements > 0:
        rapport['taux_indisponibilite'] = indisponibles / total_equipements
    else:
        rapport['taux_indisponibilite'] = 0.0

    return rapport

