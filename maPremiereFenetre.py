# -*- coding: utf-8 -*-
"""
Jean-Christophe BURNOT
16/01/22
Script de test tkinter
"""
from tkinter import Tk, Label, Button

mw = Tk()
labelHello = Label(mw, text = "Hello World !", fg = 'blue')
labelHello.pack()

buttonQuitt = Button(mw, text= "QUITTER", fg = 'red', command = mw.destroy)
buttonQuitt.pack()

mw.mainloop()



