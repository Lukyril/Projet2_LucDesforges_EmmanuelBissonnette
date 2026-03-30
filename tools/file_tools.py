"""
Auteur : Luc Desforges
Date : 17 mars 2026
Description : Contient les fonctionalités pour le traitement de fichier
"""
from pathlib import Path

#J'ai décider de d'implémenter l'outil avec la structure de classe
class File_Tools:

    #Constantes utilisées pour trouver les chemin input output, et pour les noms de fichiers exportés
    path_components = { 
        "path": "" ,
        "FILENAME" : 'input.txt',
        "INPUT_PATH" : "input/txt/",
        "EXTENSION_PATTERN" : "*.txt",
        "EXTENSION" : "TXT"
    }
    
    #Permet d'initialiser l'outil comme objet encapsulé
    def __init__(self):
        self.path_components["path"] = Path(__file__).parent.parent
    
    #Permet de chercher et de retourner le chemin vers le fichier csv dans le dossier input
    def get_path(self):
        path = Path(self.path_components["path"] / self.path_components["INPUT_PATH"])
        
        try:
            first_found_filepath = next(path.glob(self.path_components["EXTENSION_PATTERN"]))
            print(f"File found with extension '{self.path_components["EXTENSION"]}' with path: '{first_found_filepath}'")
            return first_found_filepath
        except StopIteration:
            print(f"No file found with extension '{self.path_components["EXTENSION"]}' in '{path}'")
            return None