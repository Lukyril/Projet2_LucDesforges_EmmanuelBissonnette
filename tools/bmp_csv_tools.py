"""
Auteur : Luc Desforges
Date : 17 mars 2026
Description : Contient les fonctionalités pour 
l'exportation de fichier bmp et csv à partir de l'un et l'autre
""" 
from PIL import Image

import tools.bmp_tools as bmpt
import tools.csv_tools as csvt
import pandas as pd
import numpy as np

#J'ai décider de d'implémenter l'outil avec la structure de classe
class BMP_CSV_Tools:

    msg_extension = ""
    msg_path = ""
    msg_filename = ""
    msg_e = None

    # Dictionaire de messages
    messages = {
        "FileFound": 
        f"File found with extension '{msg_extension}' with path: '{msg_path}'",
        "FileNotFoundError": 
        f"Error: The file '{msg_filename}' was not found.",
        "ValueError":
        f"Error processing image data: {msg_e}",
        "Exception":
        f"An unexpected error occurred: {msg_e}"
    }


    
    def __init__(self):
        """
        description: Permet d'initialiser l'outil comme objet encapsulé
        """

        self.bmp_tools = bmpt.BMP_Tools()
        self.csv_tools = csvt.CSV_Tools()
        


    def convert_bmp_to_csv(self):
        """
        description: Permet de convertir et d'exporter 
        un fichier bmp en un fichier csv
        """
        img = Image.open(self.bmp_tools.get_path())
        img = img.convert('L')
        img_array = np.asarray(img, dtype = int)

        self.csv_tools.export(img_array)
        


    def convert_csv_to_bmp(self, height = 20, width = 10, mode = 'L'):
        """
        description: Permet de convertir et d'exporter 
        un fichier csv en un fichier bmp
        entree: height : la hauteur de l'image, width L la largeur de l'image, 
        mode : le mode d'image (gris, en couleurs)
        """
        try:
            csv = pd.read_csv(self.csv_tools.get_path(), header=None)
            csv_array = csv.to_numpy().astype(np.uint8)
            self.bmp_tools.export(csv_array)
        #Début de fonctionalités d'exceptions requis par un critère d'évaluation
        except FileNotFoundError:
            self.msg_filename = self.csv_tools.path_components["FILENAME"]
            print(self.messages["FileNotFoundError"])
        except ValueError as e:
            self.msg_e = e
            print(self.messages["ValueError"])
        except Exception as e:
            self.msg_e = e
            print(self.messages["Exception"])
        return
