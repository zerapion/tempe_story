# player.py - Player state and character management

from dataclasses import dataclass
from typing import Dict
from .char_types import CharacterType

@dataclass
class Character:
    name: CharacterType
    stats: Dict[str, int]

class Player:
    def __init__(self):
        self.current_character = None
        self.characters = self._initialize_characters()

    def _initialize_characters(self) -> Dict[CharacterType, Character]:
        return {
            CharacterType.EVAN: Character(
                name=CharacterType.EVAN,
                stats={
                    "passion": 35,
                    "intelligence": 30,
                    "charisma": 45,
                    "strength": 10,
                    "life": 25,
                    "speed": 55,
                    "meter": 50
                }
            ),
            CharacterType.SEANH: Character(
                name=CharacterType.SEANH,
                stats={
                    "passion": 30,
                    "intelligence": 15,
                    "charisma": 5,
                    "strength": 50,
                    "life": 75,
                    "speed": 25,
                    "meter": 50     # possibly smaller starting meter for monkey
                }
            ),
            CharacterType.SEANP: Character(
                name=CharacterType.SEANP,
                stats={
                    "passion": 55,
                    "intelligence": 40,
                    "charisma": 15,
                    "strength": 20,
                    "life": 40,
                    "speed": 30,
                    "meter": 50
                }
            ),
            CharacterType.RYAN: Character(
                name=CharacterType.RYAN,
                stats={
                    "passion": 30,
                    "intelligence": 30,
                    "charisma": 25,
                    "strength": 25,
                    "life": 50,
                    "speed": 40,
                    "meter": 40
                }
            )
        }

    def select_character(self, char_type: str):
        """Select character by name string"""
        char_type = CharacterType[char_type]
        if char_type in self.characters:
            self.current_character = self.characters[char_type]
            return True
        return False

    def get_stats(self) -> Dict[str, int]:
        """Get current character's stats"""
        if self.current_character:
            return self.current_character.stats
        return {}