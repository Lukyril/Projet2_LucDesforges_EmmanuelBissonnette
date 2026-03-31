"""
Auteur : Luc Desforges
Date : 17 mars 2026
Description : Contient les fonctionalités pour le traitement de fichier csv
"""

import tools.file_tools as ft

# Hérite de la class mère File_Tools.
class EPS_Tools(ft.File_Tools):

    # Constantes utilisées pour trouver les chemins 
    # input output, et pour les noms de fichiers exportés.
    path_components = { 
        "path": "" ,
        "FILENAME" : 'input.eps',
        "INPUT_PATH" : "input/eps/",
        "EXTENSION_PATTERN" : "*.eps",
        "EXTENSION" : "EPS"
    }