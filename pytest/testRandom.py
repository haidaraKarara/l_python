#!/usr/bin/python3.6
# -*-coding:utf-8 -*
# import hashlib
# from getpass import getpass
import unittest
import random

# """ Programme testant si une an
# née est bissextile """
# def anneeBissextile():
#     annee = input("Entrer une année : ") #On attend que l'utilisateur fournit l'année qu'il désire tester
#     annee = int(annee) # Risque d'erreur si l'utilisateur ne fournit pas un nombre
#     if ((annee % 400) == 0 or (annee % 4 == 0 and annee % 100 !=  0)):
#         print("L'année saisie est bissextile.")
#     else:
#         print("L'année siaise n'est pas bissextile.")

# def chiffrememt():
#     chaineMdp = b"abcde"
#     chaineMdpChiffree = hashlib.sha1(chaineMdp).hexdigest()
#     verouille = True
#     while verouille:
#         mdpRecupere = getpass("Entrer votre mdp: ") #abcde
#         #conversion en byte 
#         mdpRecupere = mdpRecupere.encode()
#         #chiffrement
#         mdpRecupereChiffre = hashlib.sha1(mdpRecupere).hexdigest()
#         if chaineMdpChiffree == mdpRecupereChiffre:
#             verouille = False
#             print("Vous avez accès à la plate-forme !")
#         else:
#             print("Mdp incorrect.. 3 tentatives maximum.")

class RandomTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random'."""

    def setUp(self):
        """Initialisation des tests."""
        self.liste = list(range(10))

    def test_choice(self):
        """Test le fonctionnement de la fonction 'random.choice'."""
        elt = random.choice(self.liste)
        self.assertIn(elt, self.liste)

    def test_shuffle(self):
        """Test le fonctionnement de la fonction 'random.shuffle'."""
        random.shuffle(self.liste)
        self.liste.sort()
        self.assertEqual(self.liste, list(range(10)))

    def test_sample(self):
        """Test le fonctionnement de la fonction 'random.sample'."""
        extrait = random.sample(self.liste, 5)
        for element in extrait:
            self.assertIn(element, self.liste)
        #self.assertRaises(ValueError, random.sample, self.liste, 20)
        with self.assertRaises(ValueError):
            random.sample(self.liste, 20)

# if __name__ == "__main__":
#     unittest.main()