# Handles scene transitions and scene state management

from typing import Dict
from ..types.scene_types import SceneId
from ..models.scene import Scene
from ..data.scene_data import get_scenes

# scene controller
class SceneManager:
    def __init__(self):
        self.scenes: Dict[SceneId, Scene] = get_scenes()
        self.current_scene_id = SceneId.BEDROOM
    
    def get_current_scene(self) -> Scene:
        """Get the current scene object"""
        return self.scenes[self.current_scene_id]
    
    def transition_to_scene(self, scene_id: SceneId) -> bool:
        """Attempt to transition to a new scene"""
        if scene_id in self.scenes:
            self.current_scene_id = scene_id
            return True
        return False