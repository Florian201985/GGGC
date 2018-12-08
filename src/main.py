import math

from src import Parameter, Converter
from src.Flank import Flank
from src.Gear import Gear
from src.Export import Export

left_flank = Flank(Parameter.FlankSide.LEFT, Converter.grad2rad(20.0))
right_flank = Flank(Parameter.FlankSide.RIGHT, Converter.grad2rad(20.0))
z = 10
mn = 4
beta = Converter.grad2rad(10)
gear = Gear(z, mn, beta, Parameter.DirectionHelixAngle.RIGHT, left_flank, right_flank)


export = Export
export.write_dat(gear)
export.write_md(gear)
export.write_gde(gear)

