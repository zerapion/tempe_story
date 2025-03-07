# scene_data.py - Scene content and initialization data

from typing import Dict

from src.characters.enemy import EnemyType
from ..types.scene_types import SceneId, DialogueId
from ..types.action_types import Action
from ..models.scene import Scene
from ...characters.char_types import CharacterType


def get_scenes() -> Dict[SceneId, Scene]:
    """Initialize and return all game scenes"""
    return {
        SceneId.BEDROOM: Scene(
            id=SceneId.BEDROOM,
            description="You wake up and scratch your ass",
            actions=[
                Action("Scratch your ass", SceneId.BEDROOM),
                Action("Leave room", SceneId.MARGO)
            ]
        ),
        SceneId.MARGO: Scene(
            id=SceneId.MARGO,
            description="Margo common area",
            actions=[
                Action("Talk to Dr. Mario", SceneId.MARGO_DR_MARIO),
                Action("Go to the Sugar Slums", SceneId.SUGAR_SLUMS, CharacterType.EVAN),
            ]
        ),
        SceneId.MARGO_DR_MARIO: Scene(
            id=SceneId.MARGO_DR_MARIO,
            description="You approach Dr. Mario. He stares intently into your eyes.",
            initial_dialogue=DialogueId.DR_MARIO_INIT,
            actions=[
                Action("Leave", SceneId.MARGO)  # Changed from "Talk to Dr. Mario" to avoid loop
            ]
        ),
        SceneId.SUGAR_SLUMS: Scene(
            id=SceneId.SUGAR_SLUMS,
            description="You enter the Sugar Slums. The air is thick with the scent of sugar.",
            actions=[
                Action("Go to Mitchell Park", SceneId.MITCHELL_PARK, CharacterType.EVAN)
            ]
        ),
        SceneId.MITCHELL_PARK: Scene(
            id=SceneId.MITCHELL_PARK,
            description="You enter the park. You see a group of duds.",
            actions=[
                Action("Approach duds", SceneId.MITCHELL_PARK_BATTLE, CharacterType.EVAN),
            ]
        ),
        SceneId.MITCHELL_PARK_BATTLE: Scene(
            id=SceneId.MITCHELL_PARK_BATTLE,
            description="Fight!",
            actions=[],
            battle_enemy=EnemyType.DUDS
        ),
        SceneId.ZOO: Scene(
            id=SceneId.ZOO,
            description="""The Phoenix Zoo stretches before you. You can hear various animal 
            sounds in the distance.""",
            actions=[
                Action(
                    "Enter gorilla enclosure", 
                    SceneId.GORILLA_ENCLOSURE,
                    required_character=CharacterType.SEANH,
                    stat_requirements={"strength": 3}
                ),
                Action("Leave zoo", SceneId.PALM_WALK)
            ]
        ),
        # Add more scenes here
    }