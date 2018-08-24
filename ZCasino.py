#! /usr/bin/python3.6
# -*-coding:utf-8 -*

"""Jeu de roulette """
from random import randrange
from math import ceil

#Déclaration des variables de départ
argent = 1000 # on a 1000 $ au début du jeu
continuePartie = True

print("Vous démarrer la partie avec un montant de ",argent,"$\n")
while continuePartie:
    nombreMise = -1
    while nombreMise < 0 or nombreMise > 49:
        nombreMise = input("Tapez le nombre sur lequel vous misez (entre 0 et 49) : ")
        try:
            nombreMise = int(nombreMise)
        except ValueError:
            print("OUPS ! vous n'avez pas saisi un nombre.")
            nombreMise = -1
            continue
        if nombreMise < 0:
            print("Ce nombre est négatif")
        if nombreMise > 49:
            print("Ce nombre est supérieur à 49")
    # Maintenant on séléctionne la somme à miser
    mise = 0
    while mise <= 0 or mise > argent:
        mise = input("Tapez le montant de votre mise : ")
        try:
            mise = int(mise)
        except ValueError:
            print("La valeur saisie n'est pas un nombre ")
            mise = -1
            continue
        if mise <= 0:
            print("Vous avez saisi un nombre négatif ou nulle")
        if mise > argent:
            print("Impossible de miser cette somme, vous n'avez que ",argent,"$")
    # le nombre misé et la mise ont été saisi par l'utilisateur donc on fait tourner la roulette
    numeroGagnant = randrange(50)
    print("La roulette tourne... ... .. et s'arrête. Le numéro gagnant est ",numeroGagnant)

    # On établit le gain du joueur
    if numeroGagnant == nombreMise:
        print("Félicitation ! vous avez gangné")
        print("Votre avez gagné ",mise * 3)
        # On augment son argent initiale
        argent += mise * 3
    elif ( (numeroGagnant % 2 == nombreMise % 2) or (numeroGagnant % 2 != 0 and nombreMise % 2 != 0) ): # Le joueur a choisi la même couleur
        print("Vous avez misé sur la bonne couleur, vous obtenez :",mise,"$")
        # On augmente son argent
        argent += mise
    else:
        print("OH ! Pas pour cette fois, vous perdez votre mise.")
        # On diminue son argent 
        argent -= mise
    # On interrompt le jeu si le joueur est ruiné
    if argent == 0:
        print("Vous êtes ruiné, c'est la fin de la partie ! A bientôt")
        continuePartie = False
    else:
        print("Vous avez à présent une somme de :",argent,"$")
        quitter = input("Aimerez-vous quitter le Casino (o/n) ? ")
        if quitter == 'o' or quitter == 'O':
            print("Vous quittez avec une somme de : ",argent,"$")
            continuePartie = False            
   