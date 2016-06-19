from Tkinter import*
import time

tk = Tk()
canvas = Canvas(tk, width=300, height=500)
canvas.pack()

# Game speed
v = 1
# Les positions du lanceur
global x1
global y1
global x2
global y2
# L'identifiant de chaque cube
global id_cube1
global id_cube2
global id_cube3
global cube1_bouge
cube1_bouge = False
global cube2_bouge
cube2_bouge = False
global cube3_bouge
cube3_bouge = False

def creer_lanceur():
     global id_lanceur
     id_lanceur = canvas.create_rectangle(150, 450, 200, 500, fill='gray')
     x1 = 150
     y1 = 450
     x2 = 200
     y2 = 500
     canvas.bind_all('<KeyPress-w>', creer_balle)
     canvas.bind_all('<KeyPress-a>', lanceur_gauche)
     canvas.bind_all('<KeyPress-d>', lanceur_droite)

def deplacement_lanceur(distance):
     x1 += distance
     x2 += distance
     canvas.move(id_lanceur, distance, 0)

def lanceur_gauche(event):
     deplacement_lanceur(-50)

def lanceur_droite(event):
     deplacement_lanceur(50)

def creer_cubes():
     id_cube1 = canvas.create_rectangle(0, 0, 100, 100, fill='red')
     id_cube2 = canvas.create_rectangle(100, 0, 200, 100, fill='green')
     id_cube3 = canvas.create_rectangle(200, 0, 300, 100, fill='blue')

def deplacement_cube(cube):
     for x in range(0, 30):
         canvas.move(cube, 2, 0)
         tk.update()
         time.sleep(0.01 * v)
         canvas.move(cube, -4, 0)
         tk.update()
         time.sleep(0.01 * v)
         canvas.move(cube, 2, 0)
         tk.update()
         time.sleep(0.01 * v)
     for x in range(0, 50):
         canvas.move(cube, 0, -2)
         tk.update()
         time.sleep(0.002 * v)

def bouger_cube1():
     deplacement_cube(id_cube1)
     cube1_bouge = True

def bouger_cube2():
     deplacement_cube(id_cube2)
     cube2_bouge = True

def bouger_cube3():
     deplacement_cube(id_cube3)
     cube3_bouge = True

def creer_balle(event):
     id_balle = canvas.create_oval(x1, y1, x2, y2, fill='#ffd889')
     for x in range(0, 200):
         canvas.move(id_balle, 0, -2)
         tk.update()
         time.sleep(0.005 * v)
     if x1 == 0 and not cube1_bouge: bouger_cube1()
     if x1 == 50 and cube1_bouge == False:
         bouger_cube1()
     if x1 == 100 and cube2_bouge == False:
         bouger_cube2()
     if x1 == 150 and cube2_bouge == False:
         bouger_cube2()
     if x1 == 200 and cube3_bouge == False:
         bouger_cube3()
     if x1 == 250 and cube3_bouge == False:
         bouger_cube3()
     for x in range(0, 50):
         canvas.move(id_balle, 0, -2)
         tk.update()
         time.sleep(0.005 * v) 

# Initialisation
creer_cubes()
creer_lanceur()
