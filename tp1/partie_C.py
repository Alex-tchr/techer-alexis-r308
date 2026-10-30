# Partie C : manipulation des mots
import random                                       # module pour choisir un mot au hasard

# 1. liste de mots écrite directement dans le programme (un tableau)
MOTS = ["python", "ordinateur", "reseau", "clavier", "souris", "programme", "variable", "fonction"]


def charger_mots(nom_fichier):
    # 1. (autre possibilité) charger les mots depuis un fichier .txt, un mot par ligne
    liste = []
    try:
        with open(nom_fichier, "r", encoding="utf-8") as f:
            for ligne in f:
                mot = ligne.strip()                 # enlève le retour à la ligne
                if mot != "":                       # ignore les lignes vides
                    liste.append(mot)
    except OSError:
        print(f"{nom_fichier} introuvable.")        # fichier absent : pas de plantage
    if len(liste) == 0:                             # fichier absent ou vide : on prend le tableau MOTS
        print("On utilise la liste de mots du programme.")
        liste = MOTS
    return liste


def choisir_mot(liste):
    mot = random.choice(liste)                      # 2. prend un mot au hasard dans la liste
    return mot.upper()                              # et le renvoie en MAJUSCULES


def masque(mot):
    resultat = []                                   # 3. liste vide au départ
    for lettre in mot:                              # pour chaque lettre du mot...
        resultat.append("_")                        # ...on ajoute un "_"
    return resultat


# ---------- Jeu d'essai ----------
mots = charger_mots("mots.txt")                     # essaie le fichier, sinon prend le tableau MOTS
print("Liste de mots :", mots)
mot = choisir_mot(mots)
print("Mot choisi :", mot)
print("Masque :", masque(mot))
print('masque("PYTHON") ->', masque("PYTHON"))      # attendu : ['_', '_', '_', '_', '_', '_']
