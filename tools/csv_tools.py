"""
Auteur : Luc Desforges
Date : 28 mars 2026
Description : Contient les fonctionalités pour le traitement de fichier csv
"""

import numpy as np
import pandas as pd
import tools.file_tools as ft
from pathlib import Path

# Hérite de la class mère File_Tools.
class CSV_Tools(ft.File_Tools):

    # Constantes utilisées pour trouver les chemins 
    # input output, et pour les noms de fichiers exportés.
    path_components = { 
        "path": "" ,
        "FILENAME" : 'input.csv',
        "INPUT_PATH" : "input/csv/",
        "EXTENSION_PATTERN" : "*.csv",
        "EXTENSION" : "CSV"
    }


    def export(self, pixels: np.ndarray):
        """
        description: Permet d'exporter un csv à partir d'un "ndarray".
        entree: un array numpy equivalent aux pixels d'un image
        """
        # Algorithme de lecture du array afin de s'assurer 
        # qu'il soit conforme pour l'exporter en csv en 2D (sans couleurs).
        if len(pixels.shape) == 3: # Color image (H, W, C)
            # Transforme l'array en 2D exluant des artefacts de couleurs
            height, width, channels = pixels.shape
            img_array_reshape = pixels.reshape(height, width * channels)
        else: # Grayscale image (H, W)
            img_array_reshape = pixels

        df = pd.DataFrame(img_array_reshape)
        comp = self.path_components

        df.to_csv(Path(comp["path"] / comp["INPUT_PATH"]) / comp["FILENAME"], 
                  header=False, 
                  index=False)


    def change_brightness_value(self, target_value, new_value):
        """
        description: Permet de convertir un ton de gris vers 
        un autre ton de gris dans un fichier csv
        entree: target_value: ton à convertir, new_value: ton converti
        """
        csv = pd.read_csv(self.get_path(), header=None)
        csv.replace(target_value, new_value, inplace=True)
        csv_array = csv.to_numpy().astype(np.uint8)
        self.export(csv_array)