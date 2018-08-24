#! /usr/bin/python3.6
# -*-coding:utf-8 -*
from fic import Etudiant
from operator import attrgetter

#test de la fonction table

etudiants = [
    Etudiant('Thomas', 11, 14),
    Etudiant('Boubacar', 12, 18),
    Etudiant('Saliou', 11, 10),
    Etudiant('Ababacar', 14, 15)
]
l = sorted(etudiants,key=attrgetter("moyenne"),reverse=True) # Tri selon la plus forte moyenne.
for el in l:
    print(el)