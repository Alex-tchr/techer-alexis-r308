# Partie D : jeu du Pendu
import random                                       # module pour choisir un mot au hasard

ERREURS_MAX = 7                                     # nombre d'erreurs autorisées

MOTS = ["python", "ordinateur", "reseau", "clavier", "souris", "programme", "variable", "fonction", "éléphant"]

# Bonus ASCII art : un dessin par nombre d'erreurs (de 0 à 7)
# le r devant les guillemets permet d'écrire le \ sans problème
DESSINS = [
r"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
r"""
  +---+
  |   |
  X   |
 /|\  |
 / \  |
      |
=========""",
]


def enlever_accents(texte):
    # remplace les lettres accentuées par la lettre simple (É -> E) : "ÉLÉPHANT" ne fait pas planter
    accents = {"À": "A", "Â": "A", "Ä": "A", "Ç": "C", "É": "E", "È": "E", "Ê": "E", "Ë": "E",
               "Î": "I", "Ï": "I", "Ô": "O", "Ö": "O", "Ù": "U", "Û": "U", "Ü": "U", "Œ": "OE"}
    resultat = ""
    for lettre in texte:
        if lettre in accents:
            resultat = resultat + accents[lettre]   # lettre accentuée : on la remplace
        else:
            resultat = resultat + lettre            # lettre normale : on la garde
    return resultat


def choisir_mot(liste):                             # même fonction que dans la partie C
    mot = random.choice(liste)
    return mot.upper()


def masque(mot):                                    # même fonction que dans la partie C
    resultat = []
    for lettre in mot:
        resultat.append("_")
    return resultat


def demander_mot_secret():
    # bonus mode 2 joueurs : un joueur tape le mot que l'autre doit deviner
    while True:
        mot = input("Tape le mot secret (l'autre joueur ne regarde pas !) : ").strip()
        mot = enlever_accents(mot.upper())          # "Éléphant" devient "ELEPHANT"
        if mot.isalpha():                           # que des lettres (pas vide, pas de chiffre, pas d'espace)
            print("\n" * 50)                        # on "efface" l'écran pour cacher le mot
            return mot
        print("Le mot doit contenir uniquement des lettres.")


def jouer_pendu(mot):
    mot = enlever_accents(mot.upper())              # mot en MAJUSCULES et sans accents
    mot_cache = masque(mot)                         # ['_', '_', '_', ...]
    erreurs = 0
    lettres_proposees = []                          # lettres déjà tapées par le joueur

    while erreurs < ERREURS_MAX and "_" in mot_cache:   # on joue tant qu'on n'a ni gagné ni perdu
        print(DESSINS[erreurs])
        print("Mot :", " ".join(mot_cache))         # affiche par exemple "P _ _ H _ N"
        print(f"Erreurs : {erreurs}/{ERREURS_MAX}")
        print("Lettres déjà proposées :", " ".join(lettres_proposees))

        lettre = input("Propose une lettre : ").strip()
        lettre = enlever_accents(lettre.upper())    # "é" devient "E"

        if len(lettre) != 1 or not lettre.isalpha():
            print("Il faut taper une seule lettre.")            # saisie invalide : pas d'erreur comptée
        elif lettre in lettres_proposees:
            print("Lettre déjà proposée, pas d'erreur en plus.")
        elif lettre in mot:
            lettres_proposees.append(lettre)
            print("Bien vu !")
            for i in range(len(mot)):               # parcourt toutes les positions du mot
                if mot[i] == lettre:
                    mot_cache[i] = lettre           # révèle la lettre à cette position
        else:
            lettres_proposees.append(lettre)
            print("Raté !")
            erreurs = erreurs + 1                   # lettre absente : une erreur de plus

    if "_" not in mot_cache:                        # plus de "_" : toutes les lettres sont trouvées
        print("Mot :", " ".join(mot_cache))
        print("Gagné !")
        return True
    else:
        print(DESSINS[erreurs])
        print(f"Perdu, le mot était {mot}")
        return False


# ---------- Programme principal ----------
# ce bloc se lance seulement quand on exécute partie_D.py directement
# (pas quand bonus_hall_of_fame.py fait "from partie_D import ...")
if __name__ == "__main__":
    print("=== Jeu du Pendu ===")
    mode = input("1 joueur ou 2 joueurs ? (1/2) : ").strip()
    if mode == "2":
        mot_secret = demander_mot_secret()          # bonus : mode 2 joueurs
    else:
        mot_secret = choisir_mot(MOTS)              # 1 joueur : mot au hasard
    jouer_pendu(mot_secret)
