#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jean-Christophe BURNOT
16/01/22
Script de test tkinter
"""
from tkinter import Tk, Frame, Label, Button

#creation de la fenetre principale
Mafenetre = Tk()
Mafenetre.title("truc a a faire")
#couleur de fond
Mafenetre["bg"]="bisque"

#creation d'un widget frame dans la fenetre principale
Frame1 = Frame(Mafenetre, relief="groove")
Frame1.pack(side='left', padx=10, pady=10)

#creation d'un second widget dans la fenetre principale
Frame2 = Frame(Mafenetre, borderwidth=2, relief="groove")
Frame2.pack(side="left", padx=10, pady=10)

#creation d'un widget Frame dans un widget frame
#le widget Frame1 est le parent du widget Frame3
#le parent du widget Frame1 est la widget Mafenetre (fenetre principale)
Frame3 = Frame(Frame1, bg="white", borderwidth=2, relief="groove")
Frame3.pack(side="left",padx=10,pady=10)

#creation d'un widget Label et d'un widget Button dans un widget Frame
Label(Frame1,text="RDV dentiste samedi 15h").pack(padx=10, pady=10)
Button(Frame1, text="Effacer", fg="navy", command=Frame1.destroy).pack(padx=10, pady=10)

Label(Frame2, text="Reviser le controle d'info").pack(padx=10, pady=10)
Button(Frame2, text="Effacer", fg="navy", command=Frame2.destroy).pack(padx=10, pady=10)

Label(Frame3, text="Faire la fiche de SSL", bg="white").pack(padx=10, pady=10)
Button(Frame3, text="filtrer ce problème", fg="red", command=Frame3.destroy).pack(padx=10, pady=10)

Mafenetre.mainloop()