"""
Auteur : Luc Desforges
Date : 17 mars 2026
Description : Contient les fonctionalités pour l'exportation de fichier bmp et csv à partir de l'un et l'autre
""" 
from PIL import Image
import tools.bitmap_tools
import tools.eps_tools
import pandas as pd
import numpy as np

#J'ai décider de d'implémenter l'outil avec la structure de classe
class EPS_BMP_Tools:

    #Permet d'initialiser l'outil comme objet encapsulé
    def __init__(self):
        self.bmptools = tools.bitmap_tools.BMP_Tools()
        self.epstools = tools.eps_tools.EPS_Tools()
        
    #Permet de convertir et d'exporter un fichier bmp en un fichier csv
    def convert_eps_to_bmp(self):
        img = Image.open(self.epstools.get_path())
        scale_factor = 4  # e.g., scale 4x the default resolution
        img.load(scale=scale_factor) 

        img_array = np.asarray(img, dtype = int)

        self.bmptools.export(img_array)
        
   