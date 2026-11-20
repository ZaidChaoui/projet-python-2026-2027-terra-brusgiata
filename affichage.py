import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch
import numpy as np

COULEURS = [
"#D2B48C",  # 0 : VIDE (brun clair)
"#228B22",  # 1 : ARBRE (vert)
"#FF4500",  # 2 : FEU (orange vif)
"#4A4A4A",  # 3 : CENDRE (gris foncé)
]

CMAP_FORET = ListedColormap(COULEURS)

ETATS_LEGENDE = [
    (0, "Vide"),
    (1, "Arbre"),
    (2, "Feu"),
    (3, "Cendre"),
]


def _tracer_grille(ax, grille, titre=""):
    """Trace une grille sur un axe Matplotlib donné avec légende."""
    im = ax.imshow(grille, cmap=CMAP_FORET, vmin=0, vmax=3)
    ax.set_title(titre)
    ax.set_xticks([])
    ax.set_yticks([])
    patches = [
        Patch(facecolor=COULEURS[val], label=nom)
        for val, nom in ETATS_LEGENDE
    ]
    ax.legend(handles=patches, loc="upper right", framealpha=0.9)
    return im


def afficher(grille, titre=""):
    """Affiche la forêt avec ListedColormap, vmin=0, vmax=3 et une légende."""
    fig, ax = plt.subplots(figsize=(6, 6))
    _tracer_grille(ax, grille, titre=titre)
    plt.tight_layout()
    plt.show()


def afficher_trois_densites(creer_foret_fn, densites=(0.3, 0.6, 0.9), taille=(100, 100), graine=42):
    """Affiche côte à côte trois forêts de même graine et de densités différentes."""
    fig, axes = plt.subplots(1, len(densites), figsize=(5 * len(densites), 5))
    for ax, d in zip(axes, densites):
        rng = np.random.default_rng(graine)
        grille = creer_foret_fn(taille[0], taille[1], d, rng)
        _tracer_grille(ax, grille, titre=f"Densité = {d}")
    plt.tight_layout()
    plt.show()