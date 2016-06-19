from Tkinter import*
import time

tk = Tk()
canvas = Canvas(tk, width=300, height=500)
canvas.pack()

# Game speed
v = 5
# Les positions du lanceur
global x1, y1, x2, y2
# L'identifiant de chaque cube
global id_cube1, id_cube2, id_cube3
global cube1_bouge, cube2_bouge, cube3_bouge
cube1_bouge = False
cube2_bouge = False
cube3_bouge = False

def creer_lanceur():
    global id_lanceur
    global x1, y1, x2, y2
    x1 = 150
    y1 = 450
    x2 = 200
    y2 = 500
    id_lanceur = canvas.create_rectangle(x1, y1, x2, y2, fill='gray')
    canvas.bind_all('<KeyPress-w>', creer_balle)
    canvas.bind_all('<KeyPress-a>', lanceur_gauche)
    canvas.bind_all('<KeyPress-d>', lanceur_droite)

def deplacement_lanceur(distance):
    global x1, x2
    x1 += distance
    x2 += distance
    canvas.move(id_lanceur, distance, 0)

def lanceur_gauche(event):
    deplacement_lanceur(-50)

def lanceur_droite(event):
    deplacement_lanceur(50)

def creer_cubes():
    global id_cube1, id_cube2, id_cube3
    id_cube1 = canvas.create_rectangle(0, 0, 100, 100, fill='red')
    id_cube2 = canvas.create_rectangle(100, 0, 200, 100, fill='green')
    id_cube3 = canvas.create_rectangle(200, 0, 300, 100, fill='blue')

# Faire disparaître le cube en le faisant bouger
def deplacement_cube(cube):
    global id_cube1, id_cube2, id_cube3
    for x in range(0, 30):
        canvas.move(cube, 2, 0)
        tk.update()
        time.sleep(0.01 / v)
        canvas.move(cube, -4, 0)
        tk.update()
        time.sleep(0.01 / v)
        canvas.move(cube, 2, 0)
        tk.update()
        time.sleep(0.01 / v)
    for x in range(0, 50):
        canvas.move(cube, 0, -2)
        tk.update()
        time.sleep(0.002 / v)

def bouger_cube1():
    global cube1_bouge
    deplacement_cube(id_cube1)
    cube1_bouge = True

def bouger_cube2():
    global cube2_bouge
    deplacement_cube(id_cube2)
    cube2_bouge = True

def bouger_cube3():
    global cube3_bouge
    deplacement_cube(id_cube3)
    cube3_bouge = True

def creer_balle(event):
    id_balle = canvas.create_oval(x1, y1, x2, y2, fill='#ffd889')
    for x in range(0, 200 / v):
        canvas.move(id_balle, 0, -2 * v)
        tk.update()
        time.sleep(0.001)
    if (x1 == 0   or x1 == 50 ) and not cube1_bouge:
        canvas.delete(id_balle)
        bouger_cube1()
    if (x1 == 100 or x1 == 150) and not cube2_bouge:
        canvas.delete(id_balle)
        bouger_cube2()
    if (x1 == 200 or x1 == 250) and not cube3_bouge:
        canvas.delete(id_balle)
        bouger_cube3()
    for x in range(0, 50 / v):
        canvas.move(id_balle, 0, -2 * v)
        tk.update()
        time.sleep(0.001)

# Initialisation
creer_cubes()
creer_lanceur()
