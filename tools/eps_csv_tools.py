"""
Auteur : Luc Desforges
Date : 17 mars 2026
Description : Contient les fonctionalités 
pour l'exportation de fichier bmp et csv à partir de l'un et l'autre
""" 

from PIL import Image

import tools.eps_tools as epst
import tools.csv_tools as csvt
import numpy as np

#J'ai décider de d'implémenter l'outil avec la structure de classe
class EPS_CSV_Tools:

    def __init__(self):
        """
        description: Permet d'initialiser l'outil comme objet encapsulé
        """

        self.eps_tools = epst.EPS_Tools()
        self.csv_tools = csvt.CSV_Tools()
    

    def convert_eps_to_bmp(self):
        """
        description: Permet de convertir et d'exporter un fichier bmp en un fichier csv
        """

        img = Image.open(self.eps_tools.get_path())
        scale_factor = 4  # e.g., scale 4x the default resolution
        img.load(scale = scale_factor) 
        img = img.convert('RGB')
        img_array = np.asarray(img, dtype = int)
        self.csv_tools.export(img_array)