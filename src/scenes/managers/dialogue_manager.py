# Handles dialogue state and transitions

from typing import Optional, Tuple
from ..types.scene_types import SceneId, DialogueId
from ..models.dialogue import DialogueState
from ..data.dialogue_data import get_dialogues
from ...characters.char_types import CharacterType

class DialogueManager:
    def __init__(self):
        self.current_dialogue = None
        self.dialogues = get_dialogues()
    
    def start_dialogue(self, dialogue_id: DialogueId) -> DialogueState:
        """Start or transition to a new dialogue state"""
        self.current_dialogue = self.dialogues[dialogue_id]
        return self.current_dialogue
    
    def make_choice(self, choice_index: int, character: CharacterType) -> Tuple[Optional[DialogueState], Optional[SceneId]]:
        """Process player's dialogue choice and determine next state
        Returns:
        - Tuple of (next_dialogue, next_scene)
        - If next_dialogue is None but next_scene isn't: end dialogue and transition to scene
        - If next_dialogue isn't None but next_scene is None: continue dialogue
        """
        if not self.current_dialogue:
            return None, None
            
        choice = self.current_dialogue.choices[choice_index]
        
        # Handle scene transitions (both static and dynamic)
        if choice.next_scene_generator:
            return None, choice.next_scene_generator(character)
        if choice.next_scene:
            return None, choice.next_scene
            
        # Handle dialogue progression
        if choice.next_dialogue:
            return self.start_dialogue(choice.next_dialogue), None
            
        return None, None
