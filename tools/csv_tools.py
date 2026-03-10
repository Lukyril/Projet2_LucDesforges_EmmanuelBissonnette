from PIL import Image
import numpy as np
from pathlib import Path

class CSV_Tools:
    PATH = ""
    FILENAME = 'input.csv'
    INPUT_PATH = "input/csv/"
    EXTENSION_PATTERN = "*.csv"

    def __init__(self):
        self.PATH = Path(__file__).parent.parent
    
    def read(self):
        path = Path(self.PATH / self.INPUT_PATH)

        try:
            first_file = next(path.glob(self.EXTENSION_PATTERN))
            print(f"File found with extension 'csv' with path: '{first_file}'")
            return open(first_file).read()
        except StopIteration:
            print(f"No file found with extension 'csv' in '{path}'")
            return None

    def export(self, pixels: np.ndarray):
        fixed_array = pixels.reshape(-1, pixels.shape[-1] if pixels.ndim == 3 else 1)
        np.savetxt(Path(self.PATH / self.INPUT_PATH) / self.FILENAME, 
                   fixed_array, 
                   delimiter=",", 
                   fmt='%d')