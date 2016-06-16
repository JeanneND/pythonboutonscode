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
     a = len(texte)
     if a < 50:
        canvas.create_text(250, hauteur,text=texte)
     else:
        print('Cette chaîne de caractères est trop longue')

def choix_partir():
     texte('Vous incarnez un jeune homme qui se pense ', 250, True)
     texte('prêt à quitter son village', 260, False)
     texte('Le ferez-vous ?', 270, False)
     global bta
     bta = Button(tk2, text='Oui !', command=partir_en_voyage)
     bta.pack()
     global btb
     btb = Button(tk2, text='Non !', command=ne_pas_partir_en_voyage)
     btb.pack()

def partir_en_voyage():
     bta.destroy()
     btb.destroy()
     parti_en_voyage()

def ne_pas_partir_en_voyage():
     bta.destroy()
     btb.destroy()
     pas_parti_en_voyage()

def parti_en_voyage():
     texte('J\'espère que le voyage se déroulera bien.', 250, True)
     global bta
     bta = Button(tk2, text='Continuer', command=ruisseau_rencontre)
     bta.pack()

def pas_parti_en_voyage():
     texte('Puisque je reste, je peux', 250, True)
     texte('me permettre de faire', 260, False)
     texte('Une partie de pêche avec un ami !', 270, False)
     global bta
     bta = Button(tk2, text='Continuer', command=ruisseau_rencontre)
     bta.pack()

def ruisseau_rencontre():
     texte('J\'entends des bruits au bord du', 250, True)
     texte('ruisseau ...', 260, False)
     texte('Ce sont les monstres des environs.', 280, False)
     texte('Mais ils n\'attaquent pas habituellement, alors', 290, False)
     texte('qu\'ils ont capturé un homme, ', 300, False)
     texte('Qu\'est-ce que je devrais faire ?', 310, False)
     bta.destroy()
     global bta
     bta = Button(tk2, text='Se retirer', command=se_retirer_combat_riviere)
     bta.pack()
     global btb
     btb = Button(tk2, text='Se rapprocher', command=se_rapprocher_combat_riviere)
     btb.pack()

def se_retirer_combat_riviere():
     texte(' Ce combat n\'est pas le mien. Je me retire.', 100, True)
     bta.destroy()
     btb.destroy()
     global bta
     bta = Button(tk2, text='Continuer', command=rencontre_habitant_fuite_combat_riviere)

def rencontre_habitant_fuite_combat_riviere():
     texte('Je rencontre un habitant sur le chemin du retour.', 250, True)
     bta.destroy()
     global bta
     bta = Button(tk2, text='Passer à la discussion', command=discussion1replique1)
     bta.pack()

def discussion1replique1()):
     texte('Habitant : Salut !Qu\’est-ce que vous faites là ?', 250, True)
     bta.destroy()
     global bta
     bta = Button(tk2, text='Passer à la réplique suivante', command=discussion1replique2)
     bta.pack()

def discussion1replique2()):
     texte('Moi : J\ai entendu quelqu\'un dans les bois ! Des monstres!', 250, True)
     texte('Je crois qu\'ils détenaient quelqu\'un', 270, True)
     texte('Mais je préfère me retirer.C\'est plus sûr pour moi .', 290, True)
     texte('Aurevoir !', 310, True)
     bta.destroy()
     global bta
     bta = Button(tk2, text='Passer à la réplique suivante', command=discussion1replique3)
     bta.pack()   

def discussion1replique3()):
     texte('Habitant : Un instant !Je pense qu\'il s\'agit d\'Ilon, le magicien.', 250, True)
     texte('Il est de plus en plus hostile , ces temps-ci .', 270, True)
     texte('Ça ne m\'étonnerait pas de lui.Mais , vous avez raison de ne pas y aller.', 290, True)
     texte('Il est dangereux .', 310, True)
     bta.destroy()
     global bta
     bta = Button(tk2, text='Passer à la réplique suivante', command=discussion1replique4)
     bta.pack()

 def discussion1replique2()):
     texte('Moi :Merci beaucoup !', 250, True)
     texte('Je crois que je vais aller aux Champs.', 270, True)
     texte('Aurevoir !', 290, True)
     bta.destroy()
     global bta
     bta = Button(tk2, text='Aller aux Champs se divertir', command=aller_aux_champs)
     bta.pack()   

def se_rapprocher_combat_riviere():
     texte('Je suis arrivé trop tard.Il n\'y a plus que...', 100, True)
     texte('... un message de menace: ', 120, False)
     canvas.create_text(250, 200, text='N\' allez pas aux Champs', fill='red', font=('Phosphate', 24))
     canvas.create_text(250, 250, text='Sans en subir les conséquences', fill='red',  font=('Phosphate', 24))
     btb.destroy()
     bta.destroy()




choix_partir()
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

def test():
     if g2 == True:
            print('réussi')
     else:
            print('raté')
            
essai()





