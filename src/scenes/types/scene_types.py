# scene_types.py - Scene and dialogue enumeration types

from enum import Enum, auto

# scene ids ranging from 1 to n
class SceneId(Enum):
    BEDROOM = auto()
    MARGO = auto()
    MARGO_DR_MARIO = auto()
    HOMEDEPOT = auto()
    PALM_WALK = auto()  # needed for zoo exit

    """ sugar slums """
    SUGAR_SLUMS = auto()
    SUGAR_DADDYS = auto()
    MITCHELL_PARK = auto()
    MITCHELL_PARK_BATTLE = auto()
    BELOW_ETL = auto()

    """ zoo """
    ZOO = auto()
    GORILLA_ENCLOSURE = auto()

    """ ETEMP ACADEMY """
    ETEMP_ACADEMY = auto()

    LIBRARY = auto()

    """ ETEMP MARKETPLACE """
    ETEMP_MARKET = auto()

# grouped by order of occurrence
class DialogueId(Enum):
    """ DR MARIO """
    DR_MARIO_INIT = auto()
    DR_MARIO_QUEST_PROMPT = auto()
    DR_MARIO_YES = auto()
    DR_MARIO_NO = auto()

    """ HOME DEPOT """
    DESPOT_GREETING = auto()
    DESPOT_ATTACK = auto()
    DESPOT_HALF_HEALTH = auto()
    DESPOT_DEALTH = auto()

    ONLOOKER_1 = auto()
    ONLOOKER_2 = auto()



    """ SUGAR DADDY """
    """ MITCHELL PARK """
    MITCHELL_PARK_APPROACH_DUDS = auto()
