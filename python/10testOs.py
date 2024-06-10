import os
from pathlib import Path

chemin = "./Documents/doc.txt"

p = Path(chemin)  # Création d'un objet Path
p.touch(exist_ok=True)  # Création du fichier txt dans le dossier Documents
p.write_text("Hello World!")  # Écrit du texte dans le fichier
print(p.read_text())  # Lecture du contenu du fichier

print(p.name)  # Print le nom du fichier
print(p.suffix)  # Print l'extension du fichier
# help(Path.touch)

print(dir(os))
