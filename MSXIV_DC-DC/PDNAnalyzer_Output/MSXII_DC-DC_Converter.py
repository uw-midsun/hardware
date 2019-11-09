designFile = "C:/Users/Taiping/Documents/MidnightSun/hardware/MSXII_DC-DC_Converter/PDNAnalyzer_Output/MSXII_DC-DC_Converter.tgz"
powerNets = ["NetC2_2"]
groundNets = ["GND"]
excitation = [["NetC2_2", "U1", "9", "GND", "12", ""],
              ["NetC2_2", "P1", "2", "GND", "", "10.5"],
              ["NetC2_2", "P1", "3", "GND", "", "10.5"]]
# Resistors / Inductors
passives = {}
# Material Properties:
tech = [
        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'SUBSTRATE-_1', 'DielectricConstant': 4.8, 'Thickness': 0.00032004},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05}
       ]
special_settings = {'removecutoutsize' : 7.8 }
plating_thickness = 0.7
finished_hole_diameters = True