from src import Parameter, Import
from src.Export import Export
from src.Flank import Flank
from src.Gear import Gear

control_file = Import.read_ini()
control_file_data = Import.read_ste(control_file)

z = control_file_data["number of teeth"]
mn = control_file_data["normal module"]
beta = control_file_data["helix angle"]
alpha_left = control_file_data["normal pressure angle left"]
left_flank = Flank(Parameter.FlankSide.LEFT, alpha_left, beta)
alpha_right = control_file_data["normal pressure angle right"]
right_flank = Flank(Parameter.FlankSide.RIGHT, alpha_right, beta)
gear = Gear(z, mn, beta, left_flank, right_flank)


export = Export
export.write_dat(gear)
export.write_md(gear)
export.write_gde(gear)

