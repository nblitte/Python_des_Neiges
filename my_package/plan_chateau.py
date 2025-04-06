"""Niveau 1 : Construction et affichage du plan du château
   Auteur : Nathalie BLITTE
   Date : 6 Avril 2025
   Lecture du plan à partir du fichier chateau.txt, de la construction de la matrice
   correspondante pour stocker ce plan, et de son affichage grâce au module turtle.
   Entrée : Fichier plan_chateau.txt
   Sortie : Tracer chaque case à l’emplacement correspondant,
   dans une couleur correspondant à ce que dit la matrice
"""

from CONFIGS import *
from math import sqrt, floor

# En pixels, dimensions de la fenêtre d'affichage
LARGEUR_FENETRE = 290
HAUTEUR_FENETRE = 440

def lire_matrice(fichier):
    """
    Lecture du fichier plan_chateau.txt
    :param fichier: plan_chateau.txt
    :return: matrice, c’est-à-dire une liste de listes, soit une liste dont chaque élément
    sera lui-même une liste représentant une ligne horizontale de cases du plan
    """

    with open(fichier, encoding='utf-8') as fichier_in:
        return [[int(colonne) for colonne in ligne.split()] for ligne in fichier_in]

def calculer_pas(matrice):
    """
     Calcul la dimension à donner aux cases pour que le plan tienne dans la zone de la fenêtre
     turtle que nous aurons défini
    :param matrice: Résultat de la fonction lire_matrice()
    :return: Dimensions en largeur et hauteur appelé "pas", nombre de cases de la fenêtre Turtle
    en largeur, en hauteur et le nombre de cases total
    """
    # Calcul de la longueur et de la largeur de la matrice du château
    long_M = len(matrice) # 27
    larg_M = 0            # 19
    for i in range(long_M):
        larg_M = len(matrice[i])

    # Nombre de cases pour le château
    nb_max_cases = long_M * larg_M # 513 cases

    """
    Rappel des dimensions de la fenêtre Turtle 
    ZONE_PLAN_MINI = (-240, -240)  # Coin inférieur gauche de la zone d'affichage du plan
    ZONE_PLAN_MAXI = (50, 200)  # Coin supérieur droit de la zone d'affichage du plan
    soit un rectangle ABCD avec A (-240,-200), B (50,200), C (50,-240) et D (-240, -240)
    soit une fenêtre avec 290 pixels de large et 440 pixels de hauteur
    """

    # Calcul de l'aire de la fenêtre Turtle
    aire = LARGEUR_FENETRE*HAUTEUR_FENETRE

    # # Calcul de la dimension (pas) d'une case een pixels en fonction du nombre de
    # cases du château (arrondi à l'entier inférieur)
    pas = floor(sqrt(aire/ nb_max_cases)) # 15

    # Calcul du nombre de cases possibles en largeur et en hauteur pour notre fenêtre Turtle
    nb_case_la_pixels = LARGEUR_FENETRE // pas # 19
    nb_case_ha_pixels = HAUTEUR_FENETRE // pas # 29

    # Calcul du nombre de cases de la fenêtre Turtle
    nb_cases_total = nb_case_la_pixels * nb_case_ha_pixels # 551

    return pas, nb_case_la_pixels, nb_case_ha_pixels, nb_cases_total

def numerotation_cases(matrice, case, pas):
    """
    Numérotation des cases du château par un système de coordonnées
    :param case: Résultat de la fonction lire_matrice()
    :param pas: Résultat de la fonction calculer_pas()
    :return: Position de la case dans la fenêtre Turtle sous forme de tuple (x,y) :
    numéro de la ligne et de colonne (cf §7.1.3. En pratique)
    """


    # NE FONCTIONNE PAS #
    coord_x = 0
    coord_y = 0
    num_ligne = 1
    num_colonne = 1

    # Calcul de la longueur et de la largeur de la matrice du château
    long_M = len(matrice) # 27
    larg_M = 0            # 19

    for y in range(case[1]):
        larg_M = len(matrice[y])
        if coord_y < larg_M:
            chateau = [y]
            chateau.append(coord_y)
        elif coord_y >= larg_M:
            chateau = [y]
            chateau.append(coord_y + 1)
            num_colonne += 1
    print("Coordonnées de y :", coord_y)
    print("Numéro de colonne :", num_colonne)
    print(chateau)




def coordonnees(case, pas):
    """
    Calcule les coordonnées en pixels turtle du coin inférieur gauche d’une case définie
    par ses coordonnées (numéros de ligne et de colonne)
    :param case: Coordonnées d'une case définie par son numéro de ligne et de colonne : tuple
    :param pas: Résultat de la fonction calculer_pas()
    :return: Coordonnées en pixels turtle du coin inférieur gauche d’une case (numéro de ligne
     et de colonne)
    """

    coord_x = ZONE_PLAN_MINI[0] + pas
    coord_y = ZONE_PLAN_MAXI[1] - pas
    num_ligne = 0


    for x in range(larg_M):
        coord_x = case[0] + pas
        num_ligne = x + 1
        if coord_x >= ZONE_PLAN_MAXI[0]:
            num_ligne = num_ligne + 1
            coord_x = pas


    print("Coordonnées x:", coord_x)
    print("Numéro de ligne :", num_ligne) # Ne fonctionne pas






def tracer_carre(dimension):
    """
    Trace un carré
    :param dimension: Dimension en pixels turtle
    :return: Dessin Turtle d'un carré
    """

def tracer_case(case, couleur, pas):
    """
    Fonction qui appelle la fonction tracer_carre() pour tracer un carré d’une
    certaine couleur et taille à un certain endroit
    :param case: Couple de coordonnées en indice dans la matrice contenant le plan
    :param couleur: Couleur correspondant aux données issues du fichier CONFIGS.py
    :param pas: Taille d'un côté
    :return: Dessin Turtle d'un carré à une position donnée et d'une couleur donnée
    """

def afficher_plan(matrice):
    """
    Trace le plan du château à partir de la matrice obtenue de la fonction lire_matrice
    Appele la fonction tracer_case() pour chaque ligne et chaque colonne du plan, par deux
    boucles imbriquées
    :param matrice: Résultat de la fonction lire_matrice()
    :return: Tracer une case à l'emplacement correspondant dans la couleur donnée avec Turtle
    """

# MAIN DU PROGRAMME
# Lecture du fichier plan_chateau.txt
matrice = lire_matrice("plan_chateau.txt")

# Calcul de la dimension (pas) d'une case et du nombre total de cases de la fenêtre Turtle
pas, nb_case_largeur, nb_case_hauteur, nb_case_total = calculer_pas(matrice)
print(nb_case_largeur)
print(nb_case_hauteur)

# Donne les coordonnées en pixels turtle du coin inférieur gauche d’une case (numéro de ligne
#      et de colonne)
case = (19,26) # (-240,-240)

numerotation_cases(matrice, case, pas)
