"""Fichier d'installation de notre script ZCasio.py."""

from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "casino",
    version = "0.1",
    description = "Ce programme est un jeux d'ahsard",
    executables = [Executable("ZCasino.py")],
)
