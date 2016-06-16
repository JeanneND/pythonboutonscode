
global g1
g1 = False
global a1
a1 = False
global g2
g2 = False
global n1
n1 = False
def gagner(event):
     if g1 == True and a1 == True and g2 == True and n1 == True:
        texte('Gagné', 250, True)
        bta.destroy()
        btb.destroy()
        btc.destroy()
     else:
        return True    

def essai():
     canvas.bind_all('<KeyPress-c>', essai_c)
     canvas.bind_all('<KeyPress-o>', essai_o)
     canvas.bind_all('<KeyPress-d>', essai_d)
     canvas.bind_all('<KeyPress-e>', essai_e)
     canvas.bind_all('<KeyPress-t>', gagner)

def essai_c(event):
     global g1
     g1 = True

def essai_o(event):
     global a1
     a1 = True

def essai_d(event):
     global g2
     g2 = True

def essai_e(event):
     global n1
     n1 = True
        
essai()