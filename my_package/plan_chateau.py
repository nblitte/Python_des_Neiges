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

def lire_matrice(fichier):
    """
    Lecture du fichier plan_chateau.txt
    :param fichier: plan_chateau.txt
    :return: matrice, c’est-à-dire une liste de listes, soit une liste dont chaque élément
    sera lui-même une liste représentant une ligne horizontale de cases du plan
    """

    with open(fichier, encoding='utf-8') as fichier_in:
        return [[int(colonne) for colonne in ligne.split()] for ligne in fichier_in]

def afficher_plan(matrice):
    """
    Trace le plan du château à partir de la matrice obtenue de la fonction lire_matrice
    :param matrice: Résultat de la fonction lire_matrice()
    :return: Tracer une case à l'emplacement correspondant dans la couleur donnée avec Turtle
    """

# MAIN DU PROGRAMME
resultat = lire_matrice("plan_chateau.txt")
print(resultat)
