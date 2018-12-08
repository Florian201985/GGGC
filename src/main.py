import math

from src import Parameter
from src.Flank import Flank
from src.Gear import Gear

left_flank = Flank(Parameter.FlankSide.LEFT, 20.0)
right_flank = Flank(Parameter.FlankSide.RIGHT, 20.0)
z = 10
mn = 4
beta = 10 * math.pi / 180.0
gear = Gear(z, mn, beta, Parameter.DirectionHelixAngle.RIGHT, left_flank, right_flank)