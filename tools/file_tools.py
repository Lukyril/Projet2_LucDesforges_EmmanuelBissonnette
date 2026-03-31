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

    # Dictionaire de messages
    messages = {
        "FileFound": 
        "File found with extension '{msg_extension}' with path: '{msg_path}'",
        "StopIteration": 
        "No file found with extension '{msg_extension}' in '{msg_path}'"
    }



    def __init__(self):
        """
        description: Permet d'initialiser l'outil comme objet encapsulé.
        """
        self.path_components["path"] = Path(__file__).parent.parent
    


    def get_path(self):
        '''
        description: Permet de chercher et de retourner 
        le chemin vers le fichier csv dans le dossier input.

        sortie: le chemin dynamique du fichier
        '''
        comp = self.path_components
        path = Path(comp["path"] / comp["INPUT_PATH"])

        msg_path = path
        msg_extension = comp["EXTENSION"]

        try:
            first_found_filepath = next(path.glob(comp["EXTENSION_PATTERN"]))
            print(self.messages["FileFound"].format(msg_path = msg_path, 
                                                    msg_extension = msg_extension))
            return first_found_filepath
        except StopIteration:
            print(self.messages["StopIteration"].format(msg_path = msg_path, 
                                                        msg_extension = msg_extension))
            return None