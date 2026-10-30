# Partie A : dictionnaire d'étudiants
# clé = nom de l'étudiant (str), valeur = sa note (float)


def ajouter_etudiant(d, nom, note):
    try:
        note = str(note).replace(",", ".")          # accepte aussi "12,5" (virgule à la française)
        d[str(nom)] = float(note)                   # ajoute l'étudiant, ou met à jour sa note s'il existe déjà
    except ValueError:
        print(f"Note invalide pour {nom} : {note}")  # la note n'est pas un nombre : on ne l'ajoute pas
    return d


def moyenne_classe(d):
    if len(d) == 0:                                 # vérifie si le dictionnaire est vide
        print("Le dictionnaire est vide !")
        return None                                 # retourne None si le dictionnaire est vide
    else:
        somme = sum(d.values())                     # calcule la somme des notes
        moyenne = somme / len(d)                    # divise la somme par le nombre d'étudiants
        return round(moyenne, 2)                    # retourne la moyenne arrondie à 2 chiffres


def meilleur_etudiant(d):
    if len(d) == 0:                                 # vérifie si le dictionnaire est vide
        print("Le dictionnaire est vide !")
        return None                                 # retourne None si le dictionnaire est vide
    else:
        meilleur = max(d, key=d.get)                # trouve l'étudiant avec la note la plus élevée
        note = d[meilleur]                          # récupère la note de cet étudiant
        return meilleur, note                       # retourne le tuple (nom, note)


def sauvegarder(d, nom_fichier):
    try:
        with open(nom_fichier, "w", encoding="utf-8") as f:
            for nom, note in d.items():             # parcourt le dictionnaire (clé + valeur)
                f.write(f"{nom}:{note}\n")          # une ligne au format nom:note
        print(f"Sauvegarde réussie dans {nom_fichier}")
    except OSError:
        print(f"Erreur lors de la sauvegarde dans {nom_fichier}")   # message si l'écriture échoue


def recharger(nom_fichier):
    d = {}                                          # on repart d'un dictionnaire vide
    try:
        with open(nom_fichier, "r", encoding="utf-8") as f:
            for ligne in f:                         # lit le fichier ligne par ligne
                ligne = ligne.strip()               # enlève le retour à la ligne et les espaces
                morceaux = ligne.split(":")         # "Alice:12.0" devient ["Alice", "12.0"]
                if len(morceaux) == 2:
                    ajouter_etudiant(d, morceaux[0], morceaux[1])   # convertit la note en float (avec gestion d'erreur)
                else:
                    print(f"Ligne mal formée ignorée : {ligne}")
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'existe pas")     # fichier absent : pas de plantage
    except OSError:
        print(f"Erreur lors de la lecture de {nom_fichier}")
    return d


# ---------- Jeu d'essai ----------
etudiants = {}                                      # on crée un dictionnaire vide
ajouter_etudiant(etudiants, "Alice", 12)
ajouter_etudiant(etudiants, "Bob", 15)
ajouter_etudiant(etudiants, "Claire", 9.5)
print(etudiants)
print("moyenne_classe :", moyenne_classe(etudiants))        # attendu : 12.17
print("meilleur_etudiant :", meilleur_etudiant(etudiants))  # attendu : ('Bob', 15.0)

sauvegarder(etudiants, "notes.txt")                 # écrit le fichier notes.txt
etudiants_recharges = recharger("notes.txt")        # relit le fichier
print("Après rechargement :", etudiants_recharges)

# ---------- Cas qui ne doivent pas faire planter le programme ----------
print(moyenne_classe({}))                           # dictionnaire vide -> None
print(meilleur_etudiant({}))                        # dictionnaire vide -> None
recharger("fichier_absent.txt")                     # fichier absent -> message, pas de plantage
ajouter_etudiant(etudiants, "David", "abc")         # note qui n'est pas un nombre -> message

with open("notes_test.txt", "w", encoding="utf-8") as f:     # fichier avec des lignes mal formées
    f.write("Alice:12\nligne sans deux points\nBob:quinze\n")
print(recharger("notes_test.txt"))                  # ne garde que Alice
