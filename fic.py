#!/usr/bin/python3.6
# -*-coding:utf-8 -*

class Etudiant:

    def __init__(self,nom,age,moyenne):
        self.nom = nom
        self.age = age
        self.moyenne = moyenne

    def __repr__(self):
        return "Étudiant {} (âge = {}, moyenne = {})".format(self.nom,self.age,self.moyenne)
        
    def __str__(self):
        return "Étudiant {} (âge = {}, moyenne = {})".format(self.nom,self.age,self.moyenne)
    
    

    