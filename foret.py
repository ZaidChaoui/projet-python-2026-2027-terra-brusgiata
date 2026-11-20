import numpy as np

VIDE = 0
ARBRE = 1
FEU = 2
CENDRE = 3

def creer_foret(hauteur, largeur, densite, rng):
    masque_arbres = rng.random((hauteur, largeur)) < densite
    return np.where(masque_arbres, ARBRE, VIDE).astype(int)

def allumer(grille, ligne, colonne):
    grille[ligne, colonne] = FEU
    return grille

def allumer_bord_gauche(grille):
    masque_arbres = grille[:, 0] == ARBRE
    grille[masque_arbres, 0] = FEU
    return grille

def compter(grille):
    return {
        "vide": int(np.sum(grille == VIDE)),
        "arbre": int(np.sum(grille == ARBRE)),
        "feu": int(np.sum(grille == FEU)),
        "cendre": int(np.sum(grille == CENDRE)),
    }