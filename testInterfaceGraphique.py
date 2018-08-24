#! /usr/bin/python3.6
# -*-coding:utf-8 -*
from interfaceGraphique import Interface
from tkinter import *

fenetre = Tk()
interface = Interface(fenetre)
interface.mainloop()
interface.destroy()