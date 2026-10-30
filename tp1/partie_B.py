# Partie B : mini-jeu "Devine le nombre"
import random                                       # module pour tirer un nombre au hasard

ESSAIS_MAX = 10                                     # nombre d'essais autorisés


def demander_entier(message):
    while True:                                     # on redemande tant que la saisie n'est pas un nombre
        saisie = input(message)
        try:
            return int(saisie)                      # si la conversion marche, on renvoie le nombre
        except ValueError:
            print("Ce n'est pas un nombre entier, recommence.")


def jouer(mini, maxi):
    secret = random.randint(mini, maxi)             # nombre secret entre mini et maxi (inclus)
    print(f"J'ai choisi un nombre entre {mini} et {maxi}. Tu as {ESSAIS_MAX} essais.")
    essais = 0
    while essais < ESSAIS_MAX:
        proposition = demander_entier(f"Essai {essais + 1}/{ESSAIS_MAX} : ")
        essais = essais + 1                         # on compte l'essai
        if proposition < secret:
            print("Trop petit")
        elif proposition > secret:
            print("Trop grand")
        else:
            print(f"Gagné ! Trouvé en {essais} essai(s).")
            return True                             # on sort de la fonction : partie gagnée
    print(f"Perdu ! Le nombre secret était {secret}.")      # les 10 essais sont épuisés
    return False


# ---------- Programme principal ----------
rejouer = "o"
while rejouer == "o":                               # bonus : on rejoue tant que le joueur répond "o"
    choix = input("Choisir les bornes ? (o/n) : ").strip().lower()     # bonus : bornes personnalisables
    if choix == "o":
        mini = demander_entier("Borne minimum : ")
        maxi = demander_entier("Borne maximum : ")
        if mini >= maxi:                            # bornes incohérentes : on reprend 1 à 100
            print("Bornes invalides, on joue entre 1 et 100.")
            mini = 1
            maxi = 100
    else:
        mini = 1                                    # bornes de l'énoncé
        maxi = 100
    jouer(mini, maxi)
    rejouer = input("Rejouer ? (o/n) : ").strip().lower()
print("Merci d'avoir joué, au revoir !")
