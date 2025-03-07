"""
execute combat actions and handle results
"""

import random
from typing import Union
from src.characters.player import Character
from src.characters.enemy import Enemy
from src.combat.calculations.weapon_calculator import WeaponCalculator
from src.combat.models.action_result import ActionResult

class BattleAction:
    def __init__(self, actor: Union[Character, Enemy], target: Union[Character, Enemy]):
        self.actor = actor
        self.target = target
        self.weapon_calculator = WeaponCalculator()

    def execute_weapon_action(self) -> ActionResult:
        """
        execute weapon attack, generate result
        return ActionResult containing hit or miss, damage, and messages
        """

        hit_chance = self.weapon_calculator.calculate_hit_change(
            self.actor.stats, 
            self.target.stats
        )

        # roll for hit
        if random.random() <= hit_chance:
            damage = self.weapon_calculator.calculate_damage(
                self.actor.stats,
                self.target.stats
            )
            # construct ActionResult if hit lands
            return ActionResult(
                has_hit=True,
                damage=damage,
                messages=[f'{self.actor.name} does {damage} damage!']
            )
        # catch misses 
        return ActionResult(
            hit=False,
            damage=0,
            messages=[f"{self.actor.name}'s attack missed!"]
        )


