"""
Auteur : Luc Desforges
Date : 28 mars 2026
Description : Contient les fonctionalités pour le traitement de fichier csv
"""

import numpy as np
import pandas as pd
import tools.file_tools as ft
from pathlib import Path

#J'ai décider de d'implémenter l'outil avec la structure de classe
class CSV_Tools(ft.File_Tools):

    #Constantes utilisées pour trouver les chemin input output, et pour les noms de fichiers exportés
    path_components = { 
        "path": "" ,
        "FILENAME" : 'input.csv',
        "INPUT_PATH" : "input/csv/",
        "EXTENSION_PATTERN" : "*.csv",
        "EXTENSION" : "CSV"
    }
    
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
        df.to_csv(Path(self.path_components["path"] / self.path_components["INPUT_PATH"]) / self.path_components["FILENAME"], 
                  header=False, 
                  index=False)
        
    def change_brightness_value(self, target_value, new_value):
        csv = pd.read_csv(self.get_path(), header=None)
        csv.replace(target_value, new_value, inplace=True)
        csv_array = csv.to_numpy().astype(np.uint8)
        self.export(csv_array)