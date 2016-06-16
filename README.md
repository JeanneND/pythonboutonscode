# pythonboutonscode
from Tkinter import*
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
tk2 = Tk()

def partir_en_voyage():
     print('Je pars en voyage')

def ne_pas_partir():
     print('Je reste ici')

bouton1 = ['Oui', 'partir_en_voyage']
bouton2 = ['Non', 'ne_pas_partir']


def texte(texte, hauteur):
     canvas.create_rectangle(0, 0, 600, 600, fill='white')
     a = len(texte)
     if a < 50:
        canvas.create_text(250, hauteur,text=texte)
     else:
        print('Cette chaîne de caractères est trop longue')

def choix(nombre, numero1, numero2):
     if nombre >= 1:
         global bta
         bta = Button(tk2, text=numero1[0], command=numero1[1])
         bta.pack()
     if nombre >= 2:
         global btb
         btb = Button(tk2, text=numero2[0], command=numero2[1])
         btb.pack()



