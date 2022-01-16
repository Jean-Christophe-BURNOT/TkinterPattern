#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jean-Christophe BURNOT
16/01/22
Script de test tkinter
"""
from tkinter import Tk, Button, Label, StringVar
import random

def nouveauLance():
    #permet de set une valeur globale de a
    global Texte
    nb = random.randint(1, 6)
    Texte.set("Resultat ->" + str(nb))
    
Mafenetre=Tk()

Mafenetre.title("De a 6 faces")
Mafenetre.geometry('200x100+100+400')
#code poour le bouton de lance
BoutonLancer = Button(Mafenetre, text='Lancer', command = nouveauLance)
BoutonLancer.pack(side="top", padx = 5, pady = 5)
#code pour le bouton quitter
BoutonQuitter = Button(Mafenetre, text='Quitter', command = Mafenetre.destroy)
BoutonQuitter.pack(side="left", padx = 5, pady = 5)
#cree un objet associe a texte sur lequel on pourra utiliser "get" et "set"
Texte = StringVar()
#permet de faire un lance a l'ouverture du code
nouveauLance()
LabelResultat = Label(Mafenetre, textvariable = Texte, fg = "red", bg = "white")
LabelResultat.pack(side = "right", padx = 5, pady = 5)

Mafenetre.mainloop()

"""
Quel est l'utilitee d'utiliser StringVar() puisque la variable est globale?
"""