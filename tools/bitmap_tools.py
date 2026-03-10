from pathlib import Path
import numpy as np
from PIL import Image

class BMP_Tools:
    PATH = ""
    OUTPUT_PATH = "output/"
    FILENAME = 'output_image.bmp'
    INPUT_PATH = "input/bmp/"
    EXTENSION_PATTERN = "*.bmp"

    def __init__(self):
        self.PATH = Path(__file__).parent.parent

    def get_path(self): 
        path = Path(self.PATH / self.INPUT_PATH)

        try:
            first_file = next(path.glob(self.EXTENSION_PATTERN))
            print(f"File found with extension 'bmp' with path: '{first_file}'")
            return first_file
        except StopIteration:
            print(f"No file found with extension 'bmp' in '{path}'")
            return None
        
    def export(self, pixels: np.ndarray):
        image = Image.fromarray(pixels, mode='L')
        image.save(Path(self.PATH / self.OUTPUT_PATH) / self.FILENAME, format='BMP')