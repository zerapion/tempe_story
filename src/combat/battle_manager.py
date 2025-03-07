from typing import Optional
from rich.prompt import Prompt

from src.combat.actions.battle_action import BattleAction
from src.combat.models.action_result import ActionResult
from ..characters.player import Character
from ..characters.enemy import Enemy, EnemyType, get_enemy
import random

class BattleManager:
    def __init__(self):
        self.player_character: Optional[Character] = None
        self.enemy: Optional[Enemy] = None
        self.is_player_turn = False

    def initialize_battle(self, player_character: Character, enemy_type: EnemyType):
        self.player_character = player_character
        self.enemy = get_enemy(enemy_type)
        self._determine_first_turn()
        
    def _determine_first_turn(self):
        player_speed = self.player_character.stats["speed"]
        enemy_speed = self.enemy.stats["speed"]
        
        if player_speed == enemy_speed:
            self.is_player_turn = random.choice([True, False])
        else:
            self.is_player_turn = player_speed > enemy_speed

    def run_battle_turn(self, game_ui):
        if self.is_player_turn:
            # Player's turn
            game_ui.update_display(
                game_text="Your turn! Choose your action:",
                input_text="1. Attack\n2. Defend\n3. Pray\n4. Use Meter"
            )
            choice = Prompt.ask("Select action") 
            # Process player action here
        else:
            # Enemy's turn
            game_ui.update_display(
                game_text="Enemy's turn!",
                input_text="Press Enter to continue"
            )
            # Process enemy action here
            
        self.is_player_turn = not self.is_player_turn

    """
    process single weapon attack turn
    determine actor and target, execute attack (and all calculations) and apply damage
    return battle result for UI display
    """
    def process_weapon_turn(self) -> ActionResult:
        current_actor = self.player_character if self.is_player_turn else self.enemy
        target = self.enemy if self.is_player_turn else self.player_character

        action = BattleAction(current_actor, target)

        result = action.execute_weapon_action()

        # apply damage
        if result.has_hit:
            target.stats['life'] -= result.damage

        return result

