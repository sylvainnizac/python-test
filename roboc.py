#!/usr/bin/python3.4
# -*- coding: utf8 -*-

"""
Labyrinthe pour TP openclassroom
"""
 #tentative de récupération des scores d'une précédente partie
try:
    with open("scores", "rb") as Scores:
        try:
            mon_depickler = pickle.Unpickler(Scores)
            svgpartie = mon_depickler.load()
        except: #pas de sauvegarde en cours
            svgpartie = #format pas encore défini, probablement un objet particulier
except: #si le fichier est corrompu au point de ne pas pouvoir le lire ou n'existe pas
            svgpartie = #format pas encore défini, probablement un objet particulier

if svgpartie.map == None:
    choixcarte(svgpartie) #fonction du menu de choix de carte
else:
    affichcarte(svgpartie) #fonction d'affichage de la carte
    
while ??: #définir les critères de fin de partie victoire ou ordre quit
    mvt = input("dans quelle direction se déplacer?" ) #prévoir des sécurités pour entrée débile
    """
    3 types d'entrée
        direction + chiffre pour mvt robot
        "quit" pour quitter la partie
        "help" pour rappeler les commandes
    """
