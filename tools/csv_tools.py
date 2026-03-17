from PIL import Image
import numpy as np
from pathlib import Path
import pandas as pd

class CSV_Tools:
    PATH = ""
    FILENAME = 'input.csv'
    INPUT_PATH = "input/csv/"
    EXTENSION_PATTERN = "*.csv"

    def __init__(self):
        self.PATH = Path(__file__).parent.parent
    
    def get_path(self):
        path = Path(self.PATH / self.INPUT_PATH)

        try:
            first_file = next(path.glob(self.EXTENSION_PATTERN))
            print(f"File found with extension 'csv' with path: '{first_file}'")
            return first_file
        except StopIteration:
            print(f"No file found with extension 'csv' in '{path}'")
            return None

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