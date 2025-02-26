# dialogue_data.py - Dialogue content and state definitions

from typing import Dict
from ..types.scene_types import SceneId, DialogueId
from ..types.action_types import DialogueChoice
from ..models.dialogue import DialogueState
from ...characters.char_types import CharacterType

def get_dialogues() -> Dict[DialogueId, DialogueState]:
    """Initialize and return all game dialogues"""
    return {
        DialogueId.DR_MARIO_INIT: DialogueState(
            id=DialogueId.DR_MARIO_INIT,
            speaker="Dr. Mario",
            text="Good morning, chile.",
            choices=[
                DialogueChoice(
                    text="Good morning",
                    next_dialogue=DialogueId.DR_MARIO_QUEST_PROMPT,
                )
            ]
        ),
        DialogueId.DR_MARIO_QUEST_PROMPT: DialogueState(
            id=DialogueId.DR_MARIO_QUEST_PROMPT,
            speaker="Dr. Mario",
            text="Do you feel prepared?",
            choices=[
                DialogueChoice(
                    text="Yes",
                    next_dialogue=DialogueId.DR_MARIO_YES,
                ),
                DialogueChoice(
                    text="No",
                    next_dialogue=DialogueId.DR_MARIO_NO,
                )
            ]
        ),
        DialogueId.DR_MARIO_YES: DialogueState(
            id=DialogueId.DR_MARIO_YES,
            speaker="Dr. Mario",
            text_generator=lambda character: {
                CharacterType.EVAN: "*takes deep breath* Go forth my child, to the Sugar Slums",
                CharacterType.SEANH: "*takes deep breath* Go forth my child, to the Zoo",
                CharacterType.SEANP: "*takes deep breath* Go forth my child, to the Etemp Academy",
                CharacterType.RYAN: "*takes deep breath* Go forth my child, to the Etemp Marketplace"
            }[character],
            choices=[
                DialogueChoice(
                    text="Go forth",
                    next_scene_generator=lambda character: {
                        CharacterType.EVAN: SceneId.SUGAR_SLUMS,
                        CharacterType.SEANH: SceneId.ZOO,
                        CharacterType.SEANP: SceneId.ETEMP_ACADEMY,
                        CharacterType.RYAN: SceneId.ETEMP_MARKET
                    }[character]
                )
            ]
        ),
        DialogueId.DR_MARIO_NO: DialogueState(
            id=DialogueId.DR_MARIO_NO,
            speaker="Dr. Mario",
            text="You should go to Home Depot",
            choices=[
                DialogueChoice(
                    text="Go to Home Depot",
                    next_scene=SceneId.HOMEDEPOT
                )
            ]
        )
    }