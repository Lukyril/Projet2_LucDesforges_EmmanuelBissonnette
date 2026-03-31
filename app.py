import tools.bmp_csv_tools
import tools.eps_csv_tools
import tools.turtle_tools as turtle_tools
#insert turtle function call code here
global is_saved 
is_saved = False
def save_convert():
    is_saved = True
turtle_tools.final_setup()

while True:
    if is_saved == True:
        converter_eps_tool = tools.eps_csv_tools.EPS_CSV_Tools()
        converter_csv_tool = tools.bmp_csv_tools.BMP_CSV_Tools()
        converter_eps_tool.convert_eps_to_bmp()
        converter_csv_tool.convert_csv_to_bmp()
    
