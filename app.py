import tools.bmp_csv_tools
import tools.csv_tools
import numpy as np

csv_tool = tools.csv_tools.CSV_Tools()
csv_tool.change_brightness_value(255, 0)
converter_tool = tools.bmp_csv_tools.BMP_CSV_Tools()
#converter_tool.convert_bmp_to_csv()
converter_tool.convert_csv_to_bmp()