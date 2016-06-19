#!/usr/bin/env python
# -*- coding: utf-8 -*-
#pythonboutoncode
from Tkinter import*
import time
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
tk2 = Tk()
def texte(texte, hauteur, effacer):
     if effacer == True:
        canvas.create_rectangle(0, 0, 600, 600, fill='white')
     canvas.create_text(250, hauteur,text=texte)








