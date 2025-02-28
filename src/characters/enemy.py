from enum import Enum, auto
from dataclasses import dataclass
from typing import Dict
from .char_types import CharacterType

class EnemyType(Enum):
    DUDS = auto()
    ZOOKEEPER = auto()
    HOME_DEPOT_MANAGER = auto()

@dataclass
class Enemy:
    type: EnemyType
    stats: Dict[str, int]
    
def get_enemy(enemy_type: EnemyType) -> Enemy:
    """Factory function to create enemies with predefined stats"""
    enemy_stats = {
        EnemyType.DUDS: {
            "passion": 15,
            "intelligence": 20,
            "charisma": 20,
            "strength": 30,
            "life": 45,
            "speed": 20,
            "meter": 50
        }
    }
    return Enemy(type=enemy_type, stats=enemy_stats[enemy_type])
