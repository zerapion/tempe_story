# action_types.py - Action and dialogue choice dataclass definitions

from dataclasses import dataclass
from typing import Dict, Optional, Callable, List
from .scene_types import SceneId, DialogueId
from ...characters.char_types import CharacterType

@dataclass
class DialogueChoice:
    text: str                                        # what player sees in action box
    next_dialogue: Optional[DialogueId] = None       # next dialogue state if continuing conversation
    next_scene: Optional[SceneId] = None            # next scene if ending conversation
    stat_check: Optional[Dict[str, int]] = None     # required stats for this choice
    conditions: Optional[Dict[str, bool]] = None     # game state conditions
    next_scene_generator: Optional[Callable] = None  # dynamic scene transition based on character

# what appears in action box
@dataclass
class Action:
    description: str                                      # what player sees
    next_scene: SceneId                                  # where this leads
    required_character: Optional[CharacterType] = None    # character restriction
    stat_requirements: Optional[Dict[str, int]] = None   # stat requirements
    
    # check if character matches action and if they pass skill check
    def is_available(self, character: CharacterType, stats: Dict[str, int]) -> bool:
        if self.required_character and character != self.required_character:
            return False
            
        if self.stat_requirements:
            return all(stats.get(stat, 0) >= value 
                      for stat, value in self.stat_requirements.items())
        return True