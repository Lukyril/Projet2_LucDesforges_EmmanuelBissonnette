"""
Auteur : Luc Desforges
Date : 17 mars 2026
Description : Contient les fonctionalités pour l'exportation de fichier bmp et csv à partir de l'un et l'autre
""" 
from PIL import Image
import tools.bitmap_tools
import tools.csv_tools
import pandas as pd
import numpy as np

#J'ai décider de d'implémenter l'outil avec la structure de classe
class BMP_CSV_Tools:

    #Permet d'initialiser l'outil comme objet encapsulé
    def __init__(self):
        self.bmptools = tools.bitmap_tools.BMP_Tools()
        self.csvtools = tools.csv_tools.CSV_Tools()
        
    #Permet de convertir et d'exporter un fichier bmp en un fichier csv
    def convert_bmp_to_csv(self):
        img = Image.open(self.bmptools.get_path())
        img = img.convert('L')
        img_array = np.asarray(img, dtype = int)

        self.csvtools.export(img_array)
        
    #Permet de convertir et d'exporter un fichier csv en un fichier bmp
    def convert_csv_to_bmp(self, height = 20, width = 10, mode = 'L'):
        try:
            csv = pd.read_csv(self.csvtools.get_path(), header=None)
            csv_array = csv.to_numpy().astype(np.uint8)
            self.bmptools.export(csv_array)
        #Début de fonctionalités d'exceptions requis par un critère d'évaluation
        except FileNotFoundError:
            print(f"Error: The file '{self.csvtools.FILENAME}' was not found.")
        except ValueError as e:
            print(f"Error processing image data: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return
