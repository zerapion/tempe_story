# dialogue.py - Core dialogue model definition

from dataclasses import dataclass
from typing import Optional, List, Callable
from ..types.scene_types import DialogueId
from ..types.action_types import DialogueChoice
from ...characters.char_types import CharacterType

@dataclass
class DialogueState:
    id: DialogueId                           # current dialogue state
    speaker: str                             # who is talking
    text: Optional[str] = None               # static dialogue text
    text_generator: Optional[Callable] = None # dynamic text based on character
    choices: List[DialogueChoice] = None      # available responses

    def get_text(self, character: Optional[CharacterType] = None) -> str:
        """Get appropriate text based on whether it's static or dynamic"""
        if self.text_generator and character:
            return self.text_generator(character)
        return self.text or ""