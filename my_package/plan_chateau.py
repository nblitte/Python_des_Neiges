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

# En pixels, dimensions de la fenêtre d'affichage
LARGEUR_FENETRE = 290
HAUTEUR_FENETRE = 440
# Dimension de la taille d'un carré en pixels
DIMENSION = 16

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
     Ex : pour une zone turtle d’affichage pour le plan de 290 (-240 à 50) de large et
     440 (-240 à 200) de haut, si le plan fait 20 cases en largeur et 44 cases en hauteur,
     les carrés auront une taille de 10 pour ne pas sortir de la zone (ici le souci, si la
     taille est supérieure à 10, sera la hauteur du plan
    :param matrice: Résultat de la fonction lire_matrice()
    :return: Dimensions en largeur et hauteur appelé "pas", nombre de cases
    """
    # Calcul de la longueur et de la largeur de la matrice du château
    long_M = len(matrice) # 27
    larg_M = 0            # 19
    for i in range(long_M):
        larg_M = len(matrice[i])

    # Nombre de cases à obtenir
    nb_max_cases = long_M * larg_M # 513 cases

    """
    Rappel des dimensions de la fenêtre Turtle 
    ZONE_PLAN_MINI = (-240, -240)  # Coin inférieur gauche de la zone d'affichage du plan
    ZONE_PLAN_MAXI = (50, 200)  # Coin supérieur droit de la zone d'affichage du plan
    soit un rectangle ABCD avec A (-240,-200), B (50,200), C (50,-240) et D (-240, -240)
    soit une fenêtre avec 290 pixels de large et 440 pixels de hauteur
    """

    # Calcul de la dimension en fonction du nombre de cases
    dimension = (LARGEUR_FENETRE*HAUTEUR_FENETRE) // nb_max_cases
    print("Dimension", dimension)
    nb_case_la_pixels = LARGEUR_FENETRE // DIMENSION
    nb_case_ha_pixels = HAUTEUR_FENETRE // DIMENSION

    print("Total cases", nb_case_la_pixels * nb_case_ha_pixels)

    print("Nb cases en largeur : ", nb_case_la_pixels)
    print("Nb cases en hauteur : ", nb_case_ha_pixels)

    """nb_case_larg = LARGEUR_FENETRE // larg_M
    print(nb_case_larg)
    nb_case_long = HAUTEUR_FENETRE // long_M
    print(nb_case_long)
    nb_cases = nb_case_larg + nb_case_long
    print(nb_cases)
    
    # Dimensions d'une case
    dimensions = LARGEUR_FENETRE/nb_case_larg
    print(dimensions)
    dimensions = HAUTEUR_FENETRE / nb_case_long
    print(dimensions)
    """

def coordonnees(case, pas):
    """
    Calcule les coordonnées en pixels turtle du coin inférieur gauche d’une case définie
    par ses coordonnées (numéros de ligne et de colonne)
    :param case: Coordonnées d'une case définie par son numéro de ligne et de colonne : tuple
    :param pas: Résultat de la fonction calculer_pas()
    :return: Coordonnées en pixels turtle du coin inférieur gauche d’une case (numéro de ligne
     et de colonne)
    """

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
resultat = lire_matrice("plan_chateau.txt")
calculer_pas(resultat)
