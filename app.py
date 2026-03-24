import tools.bmp_csv_tools
import numpy as np

<<<<<<< Updated upstream
=======
csv_tool = tools.csv_tools.CSV_Tools()
csv_tool.change_brightness_value(0, 255)
>>>>>>> Stashed changes
converter_tool = tools.bmp_csv_tools.BMP_CSV_Tools()
converter_tool.convert_bmp_to_csv()
converter_tool.convert_csv_to_bmp()