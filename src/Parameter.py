from enum import Enum


class FlankSide(Enum):
    LEFT = 1
    RIGHT = 2


class DirectionHelixAngle(Enum):
    LEFT = -1
    RIGHT = 1


class DirectionWorm(Enum):
    LEFT = -1
    RIGHT = 1


class InternalExternal(Enum):
    INTERNAL = -1
    EXTERNAL = 1

class Precision:
    eps_normal = 0.00001
