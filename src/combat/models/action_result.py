"""
defines result of combat actions
"""

from dataclasses import datalclass, field
from typing import List

@datalclass
class ActionResult:
    has_hit: bool           # did attack land
    damage: int             # damdage dealt
    effects: List['StatusEffect'] = field(default_factory=list)
    messages: List[str] = field(default_factory=list)       # combat log messages, display in tempe story box?