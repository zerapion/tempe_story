"""
weapon calculations
"""

from typing import Dict

class WeaponCalculator:
    def calculate_hit_change(self, attacker_stats: Dict[str, int], defender_stats: Dict [str, int]) -> float:
        """
        0.5 + 0.5((attacker_speed - enemy_speed)/100)
        """
        speed_diff = attacker_stats['speed'] - defender_stats['speed']
        hit_chance = 0.5 + 0.5 * (speed_diff / 100)
        # cap value at .9, floor at .1        
        return max(.1, min(.9, hit_chance))

    def calculate_damage(self, attacker_stats: Dict[str, int], defender_stats: Dict [str, int]) -> int:
        """
        5 * ( (attacker_strength + 10) / (defender_strength + 10) )
        """
        damage = 5 * ( (attacker_stats['strength'] + 10) / (defender_stats['strength'] + 10) ) 
        # min of 1
        return max(1, round(damage))

