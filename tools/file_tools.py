"""
Auteur : Luc Desforges
Date : 17 mars 2026
Description : Contient les fonctionalités pour le traitement de fichier
"""
from pathlib import Path

# Classe mère héritée par les classes outils qui gèrent les fichiers.
class File_Tools:

    # Constantes utilisées pour trouver les chemins 
    # input output, et pour les noms de fichiers exportés.
    path_components = { 
        "path": "" ,
        "FILENAME" : 'input.txt',
        "INPUT_PATH" : "input/txt/",
        "EXTENSION_PATTERN" : "*.txt",
        "EXTENSION" : "TXT"
    }

    msg_extension = ""
    msg_path = ""

    # Dictionaire de messages
    messages = {
        "FileFound": 
        f"File found with extension '{msg_extension}' with path: '{msg_path}'",
        "StopIteration": 
        f"No file found with extension '{msg_extension}' in '{msg_path}'"
    }

    
    # Permet d'initialiser l'outil comme objet encapsulé.
    def __init__(self):
        self.path_components["path"] = Path(__file__).parent.parent
    

    # Permet de chercher et de retourner le chemin vers le fichier csv 
    # dans le dossier input.
    def get_path(self):
        comp = self.path_components
        path = Path(comp["path"] / comp["INPUT_PATH"])

        self.msg_path = path
        self.msg_extension = comp["EXTENSION"]

        try:
            first_found_filepath = next(path.glob(comp["EXTENSION_PATTERN"]))
            print(self.messages["FileFound"])
            return first_found_filepath
        except StopIteration:
            self.msg_extension = comp["EXTENSION"]
            self.msg_path = path
            print(self.messages["StopIteration"])
            return None