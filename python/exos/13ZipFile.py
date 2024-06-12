from zipfile import ZipFile
import os


# source est une référence vers le fichier zippé
source = ZipFile("./annexe/sources.zip", "r")

# extraction
source.extractall("./extraits/")

# Création des répertoires Images, Musique, Vidéos...
directory_path_images = "./extraits/Images"

try:
    os.mkdir(directory_path_images)
    print(f"Directory '{directory_path_images}' created successfully.")
except FileExistsError:
    print(f"Directory '{directory_path_images}' already exists.").mkdir(
        parents=True, exist_ok=True
    )

# Parcours du répertoire extraits/data et déplacement des fichiers en fonction de leur extension
