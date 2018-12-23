designFile = "C:/Users/Taiping/Documents/MidnightSun/hardware/MSXII_PowerDistribution/PDNAnalyzer_Output/PowerDistribution.tgz"
powerNets = ["UNPROT_12V"]
groundNets = ["GND"]
excitation = [["UNPROT_12V", "SourceVirtualComponent1", "1", "GND", "12", ""],
              ["UNPROT_12V", "U19", "1", "GND", "", "20"],
              ["UNPROT_12V", "U19", "9", "GND", "", "20"]]
# Resistors / Inductors
passives = {}
# Material Properties:
tech = [
        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05},
        {'name': 'COMPONENT_SIDE', 'Conductivity': 58800000, 'Thickness': 3.556E-05},
        {'name': 'SUBSTRATE-_1', 'DielectricConstant': 4.8, 'Thickness': 0.00032004},
        {'name': 'GROUND', 'Conductivity': 58800000, 'Thickness': 3.599E-05},
        {'name': 'SUBSTRATE-_5', 'DielectricConstant': 4.2, 'Thickness': 0.000127},
        {'name': 'SIGNAL', 'Conductivity': 58800000, 'Thickness': 3.599E-05},
        {'name': 'SUBSTRATE-_4', 'DielectricConstant': 4.2, 'Thickness': 0.000254},
        {'name': 'SOLDER_SIDE', 'Conductivity': 58800000, 'Thickness': 3.556E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05}
       ]
special_settings = {'removecutoutsize' : 7.8 }
plating_thickness = 0.7
finished_hole_diameters = True