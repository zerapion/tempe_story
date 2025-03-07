"""
define action enums
"""

from enum import Enum, auto

class ActionCategory(Enum):
    ACTION = auto()         # subtree of {STATUS, WEAPON, PERSUADE, PRAY}
    METER = auto()
    DEFEND = auto()

class SubAction(Enum):
    STATUS = auto()
    WEAPON = auto()
    PERSUADE = auto()
    PRAY = auto()
