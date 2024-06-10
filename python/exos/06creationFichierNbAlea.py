import random
from pathlib import Path

nb_1 = random.randint(0, 100)
nb_2 = random.randint(0, 100)
nb_3 = random.randint(0, 100)
nb_4 = random.randint(0, 100)
nb_5 = random.randint(0, 100)

chemin = "./Documents/nb_aleatoires.txt"

p = Path(chemin)  # Création d'un objet Path
p.touch(exist_ok=True)  # Création du fichier txt dans le dossier Documents
p.write_text(
    f"""Voici mes 5 nombres aléatoires
{nb_1},{nb_2},{nb_3},{nb_4},{nb_5}
"""
)  # Écrit du texte dans le fichier

print(p.read_text())  # Lecture du contenu du fichier

help(Path.unlink)
# Si le fichier existe bien on le supprime
""" if p.exists():
    p.unlink() """
