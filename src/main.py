from src import Parameter, Import
from src.Export import Export
from src.Flank import Flank
from src.Gear import Gear

control_file = Import.read_ini()
control_file_data = Import.read_ste(control_file)

left_flank = Flank(Parameter.FlankSide.LEFT, control_file_data["normal pressure angle left"])
right_flank = Flank(Parameter.FlankSide.RIGHT, control_file_data["normal pressure angle right"])
z = control_file_data["number of teeth"]
mn = control_file_data["normal module"]
beta = control_file_data["helix angle"]
beta_direction = control_file_data["helix angle direction"]
gear = Gear(z, mn, beta, Parameter.DirectionHelixAngle.RIGHT, left_flank, right_flank)


export = Export
export.write_dat(gear)
export.write_md(gear)
export.write_gde(gear)

