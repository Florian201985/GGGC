import math

from src import Converter


class Export:
    def __init__(self):
        pass

    def write_dat(gear):
        f = open("GeneratingGrinding.dat", "w+")
        f.write("Gear data:\n")
        f.write("   Number of teeth.............z.......: %6.2f\n" % gear.number_of_teeth)
        f.write("   Normal module...............mn......: %6.2f mm\n" % gear.normal_module)
        f.write("   Helix angle.................beta....: %6.2f °\n" % Converter.rad2grad(gear.helix_angle))
        f.write("   Pitch Diameter..............d.......: %6.2f mm\n" % gear.pitch_diameter)
        f.write("   Left Flank:\n")
        f.write("      Normal Pressure Angle....alpha_n.: %6.2f °\n" % Converter.rad2grad(gear.left_flank.pressure_angle))
        f.write("   Right Flank:\n")
        f.write("      Normal Pressure Angle....alpha_n.: %6.2f °\n" % Converter.rad2grad(gear.right_flank.pressure_angle))
        f.write("Tool data:\n")
        f.write("Process data:\n")
        f.close()

    def write_md(gear):
        f = open("GeneratingGrinding.md", "w+")
        f.write("# Generating Gear Grinding Summary\n")
        f.write("## Gear data\n")
        f.write("* Number of teeth z: %6.2f\n" % gear.number_of_teeth)
        f.write("*  Normal module m<sub>n</sub>: %6.2f mm\n" % gear.normal_module)
        f.write("*  Helix angle &beta;: %6.2f °\n" % Converter.rad2grad(gear.helix_angle))
        f.write("*  Pitch Diameter d: %6.2f mm\n" % gear.pitch_diameter)
        f.write("\n")
        f.write("### Left Flank:\n")
        f.write("* Normal Pressure Angle &alpha;<sub>n</sub>: %6.2f °\n" % Converter.rad2grad(gear.left_flank.pressure_angle))
        f.write("\n")
        f.write("### Right Flank:\n")
        f.write("* Normal Pressure Angle &alpha;<sub>n</sub>: %6.2f °\n" % Converter.rad2grad(gear.right_flank.pressure_angle))
        f.write("\n")
        f.write("## Tool data\n")
        f.write("\n")
        f.write("## Process data\n")
        f.close()

    def write_gde(gear):
        pass
