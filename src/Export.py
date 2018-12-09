import math

from src import Converter


class Export:
    def __init__(self):
        pass

    def write_dat(gear):
        f = open("GeneratingGrinding.dat", "w+")
        f.write("Gear data:\n")
        value = gear.internal_external.value * gear.number_of_teeth
        f.write("   Number of teeth...............z.......: %6.2f\n" % value)
        f.write("   Normal module.................mn......: %6.2f mm\n" % gear.normal_module)
        f.write("   Transverse module.............mt......: %6.2f mm\n" % gear.transverse_module)
        f.write("   Axial module..................mx......: %6.2f mm\n" % gear.axial_module)
        value = gear.helix_direction.value * Converter.rad2grad(gear.helix_angle)
        f.write("   Helix angle...................beta....: %6.2f °\n" % value)
        f.write("   Pitch Diameter................d.......: %6.2f mm\n" % gear.pitch_diameter)
        f.write("   Left Flank:\n")
        f.write("      Normal Pressure Angle......alpha_n.: %6.2f °\n"
                % Converter.rad2grad(gear.left_flank.normal_pressure_angle))
        f.write("      Transverse Pressure Angle..alpha_t.: %6.2f °\n"
                % Converter.rad2grad(gear.left_flank.transverse_pressure_angle))
        f.write("      Base Circle Diameter.......d_b.....: %6.2f mm\n" % gear.left_flank.base_circle_diameter)
        f.write("   Right Flank:\n")
        f.write("      Normal Pressure Angle......alpha_n.: %6.2f °\n"
                % Converter.rad2grad(gear.right_flank.normal_pressure_angle))
        f.write("      Transverse Pressure Angle..alpha_t.: %6.2f °\n"
                % Converter.rad2grad(gear.right_flank.transverse_pressure_angle))
        f.write("      Base Circle Diameter.......d_b.....: %6.2f mm\n" % gear.right_flank.base_circle_diameter)
        f.write("Tool data:\n")
        f.write("Process data:\n")
        f.close()

    def write_md(gear):
        f = open("GeneratingGrinding.md", "w+")
        f.write("# Generating Gear Grinding Summary\n")
        f.write("## Gear data\n")
        value = gear.internal_external.value * gear.number_of_teeth
        f.write("* Number of teeth z: %6.2f\n" % value)
        f.write("*  Normal module m<sub>n</sub>: %6.2f mm\n" % gear.normal_module)
        f.write("*  Transverse module m<sub>t</sub>: %6.2f mm\n" % gear.transverse_module)
        f.write("*  Axial module m<sub>a</sub>: %6.2f mm\n" % gear.axial_module)
        value = gear.helix_direction.value * Converter.rad2grad(gear.helix_angle)
        f.write("*  Helix angle &beta;: %6.2f °\n" % value)
        f.write("*  Pitch Diameter d: %6.2f mm\n" % gear.pitch_diameter)
        f.write("\n")
        f.write("### Left Flank:\n")
        f.write("* Normal Pressure Angle &alpha;<sub>n</sub>: %6.2f °\n"
                % Converter.rad2grad(gear.left_flank.normal_pressure_angle))
        f.write("* Transverse Pressure Angle &alpha;<sub>t</sub>: %6.2f °\n"
                % Converter.rad2grad(gear.left_flank.transverse_pressure_angle))
        f.write("* Base Circle Diameter d<sub>b</sub>: %6.2f mm\n"
                % gear.left_flank.base_circle_diameter)
        f.write("\n")
        f.write("### Right Flank:\n")
        f.write("* Normal Pressure Angle &alpha;<sub>n</sub>: %6.2f °\n"
                % Converter.rad2grad(gear.right_flank.normal_pressure_angle))
        f.write("* Transverse Pressure Angle &alpha;<sub>t</sub>: %6.2f °\n"
                % Converter.rad2grad(gear.right_flank.transverse_pressure_angle))
        f.write("* Base Circle Diameter d<sub>b</sub>: %6.2f mm\n"
                % gear.right_flank.base_circle_diameter)
        f.write("\n")
        f.write("## Tool data\n")
        f.write("\n")
        f.write("## Process data\n")
        f.close()

    def write_gde(gear):
        pass
