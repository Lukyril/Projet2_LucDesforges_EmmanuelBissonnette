"""
Auteur : Luc Desforges
Date : 28 mars 2026
Description : Contient les fonctionalités pour le traitement de fichier bmp
"""
from pathlib import Path
from PIL import Image

import tools.file_tools as ft
import numpy as np

# Hérite de la class mère File_Tools
class BMP_Tools(ft.File_Tools):
    
    # Constantes utilisées pour trouver les chemin 
    # input output, et pour les noms de fichiers exportés.
    path_components = { 
        "path": "" ,
        "FILENAME" : 'output_image.bmp',
        "INPUT_PATH" : "input/bmp/",
        "OUTPUT_PATH" : "output/",
        "EXTENSION_PATTERN" : "*.bmp",
        "EXTENSION" : "BMP"
    }
           
            
    """
    description: Permet d'exporter une image à partir d'un array numpy (ndarray).
    entree: pixels : un array contenant l'équivalent des pixels
    """
    def export(self, pixels: np.ndarray):
        image = Image.fromarray(pixels, mode = 'L')
        image.save(Path(self.path_components["path"] / 
                        self.path_components["OUTPUT_PATH"]) / 
                        self.path_components["FILENAME"], 
                    format = self.path_components["EXTENSION"])
