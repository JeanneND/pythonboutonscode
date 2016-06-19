from Tkinter import*
import time

tk = Tk()
canvas = Canvas(tk, width=305, height=505, bd=0, highlightthickness=0, relief='ridge')
canvas.pack()

# Game speed
v = 5
# Les positions du lanceur
global x1, y1, x2, y2
lanceur_x_gap = 10
# L'identifiant de chaque cube
global id_cube1, id_cube2, id_cube3
global cube1_bouge, cube2_bouge, cube3_bouge
cube1_bouge = False
cube2_bouge = False
cube3_bouge = False
# Balle
global id_balle, balle_existe
balle_existe = False

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
    if x1 >= lanceur_x_gap: deplacement_lanceur(-lanceur_x_gap)

def lanceur_droite(event):
    if x1 <= (300 - 50 - lanceur_x_gap) : deplacement_lanceur(lanceur_x_gap)

def creer_cubes():
    global id_cube1, id_cube2, id_cube3
    id_cube1 = canvas.create_rectangle(0, 0, 100, 100, fill='red')
    id_cube2 = canvas.create_rectangle(100, 0, 200, 100, fill='green')
    id_cube3 = canvas.create_rectangle(200, 0, 300, 100, fill='blue')

def recreer_cubes():
    global cube1_bouge, cube2_bouge, cube3_bouge
    if cube1_bouge and cube2_bouge and cube3_bouge:
        time.sleep(0.5)
        creer_cubes()
        cube1_bouge = False
        cube2_bouge = False
        cube3_bouge = False

# Faire disparaître le cube en le faisant bouger
def deplacement_cube(cube):
    global id_balle, balle_existe
    canvas.delete(id_balle)
    global id_cube1, id_cube2, id_cube3
    for x in range(0, 30 / v):
        canvas.move(cube, 2 * v, 0)
        tk.update()
        time.sleep(0.01 / v)
        canvas.move(cube, -4 * v, 0)
        tk.update()
        time.sleep(0.01 / v)
        canvas.move(cube, 2 * v, 0)
        tk.update()
        time.sleep(0.001)
    for x in range(0, 55 / v):
        canvas.move(cube, 0, -2 * v)
        tk.update()
        time.sleep(0.001)
    canvas.delete(cube)
    balle_existe = False
    recreer_cubes()

def bouger_cube1():
    global cube1_bouge
    cube1_bouge = True
    deplacement_cube(id_cube1)

def bouger_cube2():
    global cube2_bouge
    cube2_bouge = True
    deplacement_cube(id_cube2)

def bouger_cube3():
    global cube3_bouge
    cube3_bouge = True
    deplacement_cube(id_cube3)

def creer_balle(event):
    global id_balle, balle_existe
    if not balle_existe:
        id_balle = canvas.create_oval(x1, y1, x2, y2, fill='#ffd889')
        balle_existe = True
        balle_x = x1 + 25
        for i in range(0, 200 / v):
            canvas.move(id_balle, 0, -2 * v)
            tk.update()
            time.sleep(0.001)
        if (balle_x >= 0   and balle_x <= 100) and not cube1_bouge: bouger_cube1()
        if (balle_x >= 101 and balle_x <= 200) and not cube2_bouge: bouger_cube2()
        if (balle_x >= 201 and balle_x <= 300) and not cube3_bouge: bouger_cube3()
        for i in range(0, 50 / v):
            canvas.move(id_balle, 0, -2 * v)
            tk.update()
            time.sleep(0.001)
        canvas.delete(id_balle)
        balle_existe = False

# Initialisation
creer_cubes()
creer_lanceur()
