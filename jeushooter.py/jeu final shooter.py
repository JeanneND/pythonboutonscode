from Tkinter import*
import time
tk = Tk()
canvas = Canvas(tk, width=300, height=500)
canvas.pack()
global cube1_bouge
cube1_bouge = False
global cube2_bouge
cube2_bouge = False
global cube3_bouge
cube3_bouge = False
def creer_lanceur():
     global id_lanceur
     id_lanceur = canvas.create_rectangle(150, 450, 200, 500, fill='gray')
     global x1
     x1 = 150
     global y1
     y1 = 450
     global x2
     x2 = 200
     global y2
     y2 = 500
     canvas.bind_all('<KeyPress-w>', creer_balle)
     canvas.bind_all('<KeyPress-a>', lanceur_gauche)
     canvas.bind_all('<KeyPress-d>', lanceur_droite)

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

def creer_cubes():
     global id_cube1
     id_cube1 = canvas.create_rectangle(0, 0, 100, 100, fill='red')
     global id_cube2
     id_cube2 = canvas.create_rectangle(100, 0, 200, 100, fill='green')
     global id_cube3
     id_cube3 = canvas.create_rectangle(200, 0, 300, 100, fill='blue')

def bouger_cube1():
     for x in range(0, 30):
         canvas.move(id_cube1, 2, 0)
         tk.update()
         time.sleep(0.01)
         canvas.move(id_cube1, -4, 0)
         tk.update()
         time.sleep(0.01)
         canvas.move(id_cube1, 2, 0)
         tk.update()
         time.sleep(0.01)
     for x in range(0, 50):
         canvas.move(id_cube1, 0, -2)
         tk.update()
         time.sleep(0.002)
     cube1_bouge = True

def bouger_cube2():
     for x in range(0, 30):
         canvas.move(id_cube2, 2, 0)
         tk.update()
         time.sleep(0.01)
         canvas.move(id_cube2, -4, 0)
         tk.update()
         time.sleep(0.01)
         canvas.move(id_cube2, 2, 0)
         tk.update()
         time.sleep(0.01)
     for x in range(0, 50):
         canvas.move(id_cube2, 0, -2)
         tk.update()
         time.sleep(0.002)
     cube2_bouge = True

def bouger_cube3():
     for x in range(0, 30):
         canvas.move(id_cube3, 2, 0)
         tk.update()
         time.sleep(0.01)
         canvas.move(id_cube3, -4, 0)
         tk.update()
         time.sleep(0.01)
         canvas.move(id_cube3, 2, 0)
         tk.update()
         time.sleep(0.01)
     for x in range(0, 50):
         canvas.move(id_cube3, 0, -2)
         tk.update()
         time.sleep(0.002)
     cube3_bouge = True

creer_cubes()

def creer_balle(event):
     id_balle = canvas.create_oval(x1, y1, x2, y2, fill='#ffd889')
     for x in range(0, 200):
         canvas.move(id_balle, 0, -2)
         tk.update()
         time.sleep(0.005)
     if x1 == 0 and cube1_bouge == False:
         bouger_cube1()
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
         time.sleep(0.005) 

creer_lanceur()
