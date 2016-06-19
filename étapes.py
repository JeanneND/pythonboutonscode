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
     bta.pack()

def rencontre_habitant_fuite_combat_riviere():
     texte('Je rencontre un habitant sur le chemin du retour.', 250, True)
     bta.destroy()
     global bta
     bta = Button(tk2, text='Passer à la discussion', command=discussion1replique1)
     bta.pack()



def discussion1replique1():
     texte('''Habitant : Salut !Qu’est-ce que vous faites là ?''', 250, True)
     bta.destroy()
     global bta
     bta = Button(tk2, text='Passer à la réplique suivante', command=discussion1replique2)
     bta.pack()

def discussion1replique2():
     texte('Moi : J\ai entendu quelqu\'un dans les bois ! Des monstres!', 250, True)
     texte('Je crois qu\'ils détenaient quelqu\'un ', 270, False)
     texte('Mais je préfère me retirer.C\'est plus sûr pour moi .', 290, False)
     texte('Aurevoir !', 310, False)
     bta.destroy()
     global bta
     bta = Button(tk2, text='Passer à la réplique suivante', command=discussion1replique3)
     bta.pack()   

def discussion1replique3():
     texte('Habitant : Un instant !Je pense qu\'il s\'agit d\'Ilon, le magicien.', 250, True)
     texte('Il est de plus en plus hostile , ces temps-ci .', 270, False)
     texte('Ça ne m\'étonnerait pas de lui.Mais , vous avez raison de ne pas y aller.', 290, False)
     texte('Il est dangereux .', 310, False)
     bta.destroy()
     global bta
     bta = Button(tk2, text='Passer à la réplique suivante', command=discussion1replique4)
     bta.pack()

def discussion1replique4():
     texte('Moi :Merci beaucoup !', 250, True)
     texte('Je crois que je vais aller aux Champs.', 270, False)
     texte('Aurevoir !', 290, False)
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
     global bta
     bta = Button(tk2, text='Aller aux Champs', command=aller_aux_champs)
     bta.pack()
     global btb
     btb = Button(tk2, text='prevenir le village', command=prev_village)
     btb.pack()

def prev_village():
     texte('''Ce combat n’est pas le mien .Je me retires , mais ,''', 125, True)
     texte(''' cachés derrière un arbre, deux enfants m’attendent.Bon.''', 150, False)
     texte('''-Salut !Qu’est-ce que vous faites là ?''', 225, False)
     texte('''-Oh… C’est à dire que… Eh bien,''', 250, False )
     texte('''vous n’allez sans doute pas me croire,''', 275, False)
     texte(''' mais j’ai entendu des cris et vu un message''', 300, False)
     texte(''' dans les bois. Je m’en vais en faire part au village''', 325, False)
     texte('''-Quelque chose me dit que le magicien Ilon est dans le coup.''', 350, False)
     texte(''' Il est en mauvais termes avec nous en ce moment''', 375, False)
     texte(''' et je le vois bien déposer un message de menace.''', 400, False)
     texte('''Ce serait tout à fait lui.Si j’était vous, j’irais aux Champs.''', 425, False)
     texte('''C’est votre seule piste et j’ai entendu dire qu’il y traîne parfois.''', 450, False)
     texte('''-Merci beaucoup !''', 475, False)
     bta.destroy()
     btb.destroy()
     global bta
     bta = Button(tk2, text='Aller aux Champs', command=aller_aux_champs)
     bta.pack()

def aller_aux_champs():
     texte('Je vais aux Champs', 250, True)
     texte('Mais je n\'ai pas le temps de me défendre que déjà', 275, False)
     bta.destroy()
     
