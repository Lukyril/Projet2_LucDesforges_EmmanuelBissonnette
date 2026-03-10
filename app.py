import tools.csv_tools
import numpy as np

csvtools = tools.csv_tools.CSV_Tools()
csvtools.export(np.array([1,2,3], dtype=np.uint8))