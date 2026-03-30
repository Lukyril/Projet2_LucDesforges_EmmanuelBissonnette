"""
Auteur : Luc Desforges
Date : 17 mars 2026
Description : Contient les fonctionalités pour l'exportation de fichier bmp et csv à partir de l'un et l'autre
""" 
from PIL import Image

import tools.bitmap_tools as bmpt
import tools.csv_tools as csvt
import pandas as pd
import numpy as np

#J'ai décider de d'implémenter l'outil avec la structure de classe
class BMP_CSV_Tools:

    #Permet d'initialiser l'outil comme objet encapsulé
    def __init__(self):
        self.bmp_tools = bmpt.BMP_Tools()
        self.csv_tools = csvt.CSV_Tools()
        
    #Permet de convertir et d'exporter un fichier bmp en un fichier csv
    def convert_bmp_to_csv(self):
        img = Image.open(self.bmp_tools.get_path())
        img = img.convert('L')
        img_array = np.asarray(img, dtype = int)

        self.csv_tools.export(img_array)
        
    #Permet de convertir et d'exporter un fichier csv en un fichier bmp
    def convert_csv_to_bmp(self, height = 20, width = 10, mode = 'L'):
        try:
            csv = pd.read_csv(self.csv_tools.get_path(), header=None)
            csv_array = csv.to_numpy().astype(np.uint8)
            self.bmp_tools.export(csv_array)
        #Début de fonctionalités d'exceptions requis par un critère d'évaluation
        except FileNotFoundError:
            print(f"Error: The file '{self.csv_tools.FILENAME}' was not found.")
        except ValueError as e:
            print(f"Error processing image data: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return