#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jean-Christophe BURNOT
16/01/22
Script de test tkinter
"""
from tkinter import Tk, Canvas, Button

def Clavier(event):
    global PosX,PosY
    touche = event.keysym
    print(touche)
    
    if touche == "a":
        PosY -=20
    
    if touche == "q":
        PosY+=20
        
    if touche == "m":
        PosX +=20
        
    if touche == "l":
        PosX -= 20
    
    Canvas.coords(Pion, PosX-10, PosY-10, PosX+10, PosY+10)

Mafenetre = Tk()
Mafenetre.title("Pion")

PosX = 230
PosY = 150

Largeur=480
Hauteur=320
Canevas = Canvas(Mafenetre, width=Largeur, height=Hauteur, bg="white")
Pion = Canevas.create_oval(PosX-10, PosY-10, PosX+10, PosY+10,width=5, outline="black",fill="red")
Canevas.focus_set()
Canevas.bind('<key>', Clavier)
Canevas.pack(padx=5,pady=5)

Button(Mafenetre, text="Quitter", command=Mafenetre.destroy).pack(side="left",padx=5,pady=5)

Mafenetre.mainloop()

