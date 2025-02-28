# scene.py - Core scene model definition

from dataclasses import dataclass
from typing import List, Optional, Dict

from src.characters.enemy import EnemyType
from ..types.scene_types import SceneId, DialogueId
from ..types.action_types import Action
from ...characters.char_types import CharacterType

# what appears in tempe quest box
@dataclass
class Scene:
    id: SceneId
    description: str
    actions: List[Action]                            # available actions
    initial_dialogue: Optional[DialogueId] = None    # dialogue to start when entering scene
    battle_enemy: Optional[EnemyType] = None

    # return list of available actions based off of character and stats
    def get_available_actions(self, character: CharacterType, stats: Dict[str, int]) -> List[Action]:
        return [action for action in self.actions 
                if action.is_available(character, stats)]
