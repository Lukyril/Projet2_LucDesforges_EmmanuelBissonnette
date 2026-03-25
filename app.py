import tools.bmp_csv_tools
import tools.eps_bmp_tools
import numpy as np


#insert turtle function call code here


converter_eps_tool = tools.eps_bmp_tools.EPS_BMP_Tools()
converter_csv_tool = tools.bmp_csv_tools.BMP_CSV_Tools()
converter_eps_tool.convert_eps_to_bmp()
converter_csv_tool.convert_bmp_to_csv()
converter_csv_tool.convert_csv_to_bmp()