"""
Auteur : Luc Desforges
Date : 17 mars 2026
Description : Contient les fonctionalités pour le traitement de fichier csv
"""
from PIL import Image
import numpy as np
from pathlib import Path
import pandas as pd

#J'ai décider de d'implémenter l'outil avec la structure de classe
class EPSTools:
    #Constantes utilisées pour trouver les chemin input output, et pour les noms de fichiers exportés
    PATH = ""
    FILENAME = 'input.eps'
    INPUT_PATH = "input/eps/"
    EXTENSION_PATTERN = "*.eps"

    #Permet d'initialiser l'outil comme objet encapsulé
    def __init__(self):
        self.PATH = Path(__file__).parent.parent

    #Permet de chercher et de retourner le chemin vers le fichier csv dans le dossier input
    def get_path(self):
        path = Path(self.PATH / self.INPUT_PATH)

        try:
            first_found_filepath = next(path.glob(self.EXTENSION_PATTERN))
            print(f"File found with extension 'eps' with path: '{first_found_filepath}'")
            return first_found_filepath
        except StopIteration:
            print(f"No file found with extension 'eps' in '{path}'")
            return None
    
    #TODO
    #Permet d'exporter un csv à partir d'un array numpy (ndarray)  
    def export(self, pixels: np.ndarray):
         # Reshape the array for CSV export
        if len(pixels.shape) == 3: # Color image (H, W, C)
            # Reshape from 3D (height, width, channels) to 2D (height, width*channels)
            height, width, channels = pixels.shape
            print(pixels.shape)
            img_array_reshape = pixels.reshape(height, width*channels)
        else: # Grayscale image (H, W)
            img_array_reshape = pixels

        df = pd.DataFrame(img_array_reshape)
        df.to_csv(Path(self.PATH / self.INPUT_PATH) / self.FILENAME, 
                  header=False, 
                  index=False)
