# -*-coding:utf-8 -*

import os
import pickle
import random
# import fonctions

# Inscription du joueur. 
# On rappatrie le score du joueur. S'il est inconnu, on lui met zéro.

joueur = input("saisissez le nom du joueur : ")
score = 0
histoscore_recupere = {}

try:
    with open('donnees', 'rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        histoscore_recupere = mon_depickler.load()
except FileNotFoundError:
    print("fichier non trouvé")
    histoscore_recupere[joueur] = 0

try:
    score = histoscore_recupere[joueur]
    print("Bonjour {}, votre score est de {}.".format(joueur, str(score)))
except KeyError:
    histoscore_recupere[joueur] = 0


mots = ["cheval", "oiseau", "chameau", "orange", "banane", "fraise", "hibou",
"genou", "maman", "cirque", "quand"]

    
# On affiche le mot à deviner et le nombre de chances restant, les lettres sont
# masquées par des étoiles.


# Le joueur propose une lettre.

# Si la lettre correspond à une lettre du mot, elle y remplace l'étoile, pour 
# chaque lettre du mot.
# Sinon, on décompte une chance.
# On affiche le mot à deviner et le nombre de chances restant, les lettres sont
# masquées par des étoiles.

while True:
    chances = 8
    mot = random.choice(mots)
    cachemot = ""
    tentatives = []
    for lettre in mot:
        cachemot += "*"

    #print(mot)
    print(cachemot)

    lettresAtrouver = len(mot)
    lettresTrouvees = 0
    gain = True

    while lettresTrouvees < lettresAtrouver: 
        penalite = 1
        compteur = 0
        while True:
            tentative = (input("propose une lettre : ")).lower()
            if len(tentative) != 1:
                print("saisir une et une seule lettre")
                continue
            if len([ii for ii in tentatives if ii == tentative]) == 1:
                print("{} déjà essayé. Faire une autre lettre.". \
                format(tentative))
                continue
            else:
                tentatives.append(tentative)
                break        
        for lettre in mot:
            #print(compteur)
            if tentative == lettre:
                lettresTrouvees += 1
                penalite = 0
                print("good !")
                cachemot = cachemot[0:compteur] + tentative + \
                cachemot[(compteur+1):lettresAtrouver]
                print(cachemot)
            compteur += 1
        if penalite != 0:
            print("mauvais choix")
        chances += - penalite
        print("Il ne reste plus que {} chance(s).".format(chances))
    # Si le nombre de chances tombe à 0, le jeu s'arrête.
        if chances == 0:
            gain = False
            print("pendu ! Il fallait trouver {}.".format(mot))
            break
    if gain:
        score += chances
        print("nouveau score : {}".format(score))
    continuer = input("""appuyez sur y pour continuer, ou n'importe quelle
    touche pour arrêter : """)
    if continuer != "y":
        histoscore_recupere[joueur] = score
        with open('donnees', 'wb') as fichier:
            mon_pickler = pickle.Pickler(fichier)
            mon_pickler.dump(histoscore_recupere)
        print("fin du jeu")
        break

# Une nouvelle partie est proposée.

# Si le nombre de chances tombe à 0, le jeu s'arrête.

# Une nouvelle partie est proposée.

# Le jeu s'arrête quand le joueur refuse la proposition de continuer.
# Le score est enregistré.

os.system("pause")