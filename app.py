import tools.bmp_csv_tools
import tools.eps_csv_tools
import tools.turtle_tools
#insert turtle function call code here

tools.turtle_tools.final_setup()

while tools.turtle_tools.is_saved == True:
    converter_eps_tool = tools.eps_csv_tools.EPS_CSV_Tools()
    converter_csv_tool = tools.bmp_csv_tools.BMP_CSV_Tools()
    converter_eps_tool.convert_eps_to_bmp()
    converter_csv_tool.convert_csv_to_bmp()
    tools.turtle_tools.is_saved = False
    
