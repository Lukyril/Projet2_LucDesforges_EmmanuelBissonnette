"""
Auteur : Luc Desforges
Date : 17 mars 2026
Description : Contient les fonctionalités pour le traitement de fichier bmp
"""
from pathlib import Path
import numpy as np
from PIL import Image

#J'ai décider de d'implémenter l'outil avec la structure de classe
class BMP_Tools:
    #Constantes utilisées pour trouver les chemin input output, et pour les noms de fichiers exportés
    PATH = ""
    OUTPUT_PATH = "output/"
    FILENAME = 'output_image.bmp'
    INPUT_PATH = "input/bmp/"
    EXTENSION_PATTERN = "*.bmp"
    
    #Permet d'initialiser l'outil comme objet encapsulé
    def __init__(self):
        self.PATH = Path(__file__).parent.parent
    
    #Permet de chercher et de retourner le chemin vers le fichier bmp dans le dossier input
    def get_path(self): 
        path = Path(self.PATH / self.INPUT_PATH)

        try:
            first_file = next(path.glob(self.EXTENSION_PATTERN))
            print(f"File found with extension 'bmp' with path: '{first_file}'")
            return first_file
        except StopIteration:
            print(f"No file found with extension 'bmp' in '{path}'")
            return None
            
    #Permet d'exporter une image à partir d'un array numpy (ndarray)  
    def export(self, pixels: np.ndarray):
        image = Image.fromarray(pixels, mode='L')
        image.save(Path(self.PATH / self.OUTPUT_PATH) / self.FILENAME, format='BMP')
