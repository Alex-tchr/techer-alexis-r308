# Bonus : Jeu 1 (hall of fame) et Jeu 2 (tournoi du Pendu)
from partie_D import MOTS, choisir_mot, demander_mot_secret, jouer_pendu   # on réutilise le pendu de la partie D

FICHIER_SCORES = "scores.txt"


def charger_scores(nom_fichier):
    scores = {}                                     # dictionnaire nom -> nombre de victoires
    try:
        with open(nom_fichier, "r", encoding="utf-8") as f:
            for ligne in f:
                ligne = ligne.strip()
                morceaux = ligne.split(":")         # "Ana:2.0" devient ["Ana", "2.0"]
                if len(morceaux) == 2:
                    try:
                        scores[morceaux[0]] = float(morceaux[1])
                    except ValueError:
                        print(f"Ligne ignorée : {ligne}")   # le nombre de victoires n'est pas un nombre
                else:
                    print(f"Ligne mal formée ignorée : {ligne}")
    except FileNotFoundError:
        print("Pas encore de scores.txt : tout le monde part de zéro.")
    except OSError:
        print(f"Erreur lors de la lecture de {nom_fichier}")
    return scores


def sauvegarder_scores(scores, nom_fichier):
    try:
        with open(nom_fichier, "w", encoding="utf-8") as f:
            for nom, victoires in scores.items():
                f.write(f"{nom}:{victoires}\n")     # une ligne par joueur, ex : Ana:2.0
    except OSError:
        print(f"Erreur lors de la sauvegarde dans {nom_fichier}")


def afficher_scores(scores):
    print("=== Hall of fame ===")
    if len(scores) == 0:
        print("Aucun score pour l'instant.")
    for nom in sorted(scores, key=scores.get, reverse=True):   # du plus de victoires au moins
        print(f"{nom} : {scores[nom]} victoire(s)")


def demander_nom():
    nom = input("Ton prénom : ").strip()
    while nom == "" or ":" in nom:                  # le ":" casserait le format du fichier
        nom = input("Prénom invalide, recommence : ").strip()
    return nom


# ---------- Programme principal ----------
scores = charger_scores(FICHIER_SCORES)             # relit les scores au lancement
afficher_scores(scores)

rejouer = "o"
while rejouer == "o":
    nom = demander_nom()
    mode = input("1 = mot au hasard, 2 = tournoi (ton voisin choisit le mot) : ").strip()
    if mode == "2":
        mot = demander_mot_secret()                 # Jeu 2 : le voisin tape le mot
    else:
        mot = choisir_mot(MOTS)

    gagne = jouer_pendu(mot)
    if nom not in scores:
        scores[nom] = 0.0                           # nouveau joueur : 0 victoire
    if gagne:
        scores[nom] = scores[nom] + 1               # une victoire de plus

    rejouer = input("Rejouer ? (o/n) : ").strip().lower()

sauvegarder_scores(scores, FICHIER_SCORES)          # réécrit le fichier à la fin
afficher_scores(scores)
