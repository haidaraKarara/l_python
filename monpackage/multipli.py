#! /usr/bin/python3.6
# -*-coding:utf-8 -*
""" Module multipli contenant la fonction table """

def table(nombre,max=10):
    """ Fonction affichant la table de multiplication par
        nombre jusqu'à nombre * max """ 
    i = 0
    while i < max:
        print( i + 1," * ",nombre," = ",(i + 1) * nombre)
        i += 1

if __name__ == "__main__":
    print("Pour exécuter ce programme vous devez exécuter le fichier test.py")