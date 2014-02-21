# -*- coding: latin-1 -*-

import os
from random import randrange

print "Bienvenue au Casino Jay "
reponse_ok=False
argent=0
reponse=raw_input("Voulez vous jouer une partie ? Taper O pour Oui N pour Non. ")
while reponse_ok == False :
    reponse_traiter= reponse.lower()
    if reponse_traiter=="o":
        print "la partie va commencer."
        argent=1000
        continuer_parti=True
        reponse_ok = True
    elif reponse_traiter=="n" :
        print "D'accord au revoir"
        continuer_parti=False
        break
    else:
        reponse=raw_input("Votre choix n'est pas valide, taper O pour Oui N pour Non.")
        reponse_ok=False
while continuer_parti==True :
    nombre_choisi = -1
    while nombre_choisi < 0 or nombre_choisi > 49:  
        nombre_choisi= raw_input("Veuillez choisir un nombre entre 0 et 50 : ")
        try :
            nombre_choisi=int(nombre_choisi)
        except ValueError:
            print "vous n'avez pas saisie de nombre"
            nombre_choisi = -1
            continue    
        if nombre_choisi < 0 :
            print "le nombre choisi ne peux pas être négatif"
        if nombre_choisi >49 :
            print"Le nombre choisi ne peux pas être plus grand que 49"
    la_mise = -1
    while la_mise < 1 or la_mise > argent :
        print "Vous avez ",argent," $."
        la_mise = raw_input("Combien voulez-vous miser ? : ")
        try :
            la_mise=int(la_mise)
        except ValueError:
            print "vous n'avez pas saisie de nombre"
            la_mise = -1 
            continue
        if la_mise < 1 :
            print "la mise minimum est de 1 $"
        if la_mise > argent :
            print"Tu ne peux pas miser autant le pauvre !!!"

    numero_gagnant = randrange(50)
    print"La roulette tourne... ... et arrête sur le chiffre", numero_gagnant
    if numero_gagnant == nombre_choisi :
        argent = argent + (la_mise*3)
        print "Bravo !!! Vous avez Gagnez ",(la_mise*3)," $."
        print "Vous avez maintenant", argent, " $."
    elif numero_gagnant % 2 == nombre_choisi % 2 :
        argent = argent + (la_mise*0.5)
        print "Bravo !!! Vous avez Gagnez ",(la_mise*0.5)," $."
        print "Vous avez maintenant", argent, " $."
    else :
        argent = argent - la_mise
        print "HaHa tu as perdu sale loser !!! Vous avez perdu ",la_mise," $."
        print "Vous avez maintenant", argent, " $."
    reponse_ok = False
    while reponse_ok == False :
        reponse_continuer = raw_input ("Voulez vous continuez ? (O ou N) : ")
        if reponse_continuer.lower() == "o" :
            reponse_ok = True
            continuer_parti=True
        elif reponse_continuer.lower() == "n" :
            print "D'accord, au revoir. Vous avez terminez la partie avec ", argent, " $."
            continuer_parti=False
            reponse_ok = True
        else:
            print "Votre réponse n'est pas valide. Recommencer"
            reponse_ok = False
