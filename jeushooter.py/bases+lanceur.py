from Tkinter import*
import time
tk = Tk()
canvas = Canvas(tk, width=300, height=500)
canvas.pack()

def creer_lanceur():
     global id_lanceur
     id_lanceur = canvas.create_rectangle(125, 450, 175, 500, fill='gray')
     global x1
     x1 = 125
     global y1
     y1 = 450
     global x2
     x2 = 175
     global y2
     y2 = 500
     canvas.bind_all('<KeyPress-w>', creer_balle)
     canvas.bind_all('<KeyPress-a>', lanceur_gauche)
     canvas.bind_all('<KeyPress-d>', lanceur_droite)

def creer_balle(event):
     id_balle = canvas.create_oval(x1, y1, x2, y2, fill='#ffd889')
     for x in range(0, 500):
         canvas.move(id_balle, 0, -1)
         tk.update()
         time.sleep(0.002)


    
def lanceur_gauche(event):
     global x1
     x1 = x1 - 50
     global x2
     x2 = x2 - 50
     canvas.move(id_lanceur, -50, 0)



def lanceur_droite(event):
     global x1
     x1 = x1 + 50
     global x2
     x2 = x2 + 50
     canvas.move(id_lanceur, 50, 0)

creer_lanceur()
