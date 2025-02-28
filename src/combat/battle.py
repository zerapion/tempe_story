""" 
battle flow:
  get character and enemy stats

  notes:
    roll at same time to check priority
        both players roll, once move order is detemined (considering priority), calculate damages as stats might change after move 1
                        PAS INT 
    DUDS STATS: Duds	PAS = 15 INT = 20 CHA = 20 STR = 30	HEALTH =45	SPEED = 20
  runthrough with evan
    0. speed check to determine whose first, evan is determined to move first (ptr to char)
    // calc for prayer values at start of value? set flag for if passion changes and prayer p's need to be recalced
    // this might be changed to only calc with base passion
    
    1. evan prays (roll for prayer type) and gets a stat increase (roll for which stat) to str
        str is increased to 42
        duds rolled for action, got attack, rolled probability of landing, failed roll
    
    2. evans turn and choose weapon, calculate chance to hit (if it hits), hit lands -> calculate damange (when it hits)
        duds rolled for prayer, rolled for prayer type and got meter sap
        evan lost 3 fructose, 47 remaining ( consider how meter works )
  
    3. evan chooses status, the next time evan takes damage from enemy attack he will absorb .375 
        duds rolled for prayer, roll for prayer type and got stat boost for passion

    4. evan choose pray (duds roll status, no priority so evan moves first), 
        rolled and got stat increase to PAS by 23 for 58 total passion
        duds use their status to apply poison for 3 turns to evan
        evan takes poisson damage
        
        
    5. evan choose weapon, duds roll and get defend->meditate so duds move first but do nothing cause it did not nullify a prayer
        evan does his weapon so roll for if it hits, it hits, calc damage
        evan takes poisson damage
   
    
    6. evan chooses weapon and duds roll weapon so evan moves first
            evan roll for if it hits, then calc damage if it does
            duds roll for if it hits, then calc damage if it does

    7. evan chooses weapon, duds roll status
        evan rolls for if it hits, calc damage
        duds hit status, calc posion damage on evan (lasts 3 turns)
        evan takes poisson
 
    8. evan chooses weapon, duds roll to parry
        parry lands, evan does no damage and will bestunned next turn, duds get +50 str next turn
        evan takes poisson damage
 
    9. because parry hit, duds do weapon, roll for if it hits, calc damage (consider temp stat changes)
        evan takes 9 damage
        evan takes poisson damage, left with 9 health, poisson dissapates
        
    10. evan does prayer, duds roll dodge so move first but do nothing
            roll for what type of prayer, got heal, calc heal amount
 
    11. evan chooses meter, duds roll weapon
            calc evans meter attack and do damage to duds, remove 30 meter
            duds roll meter, roll for if it hits, calc hit damage
 
    12. evan chooses persuade, duds roll prayer (roll for prayer type, got smite)
            evan moves first, calc if persuades hit ( was a small chance, but he does persuade)
            duds are persuaded, battle ends
"""

"""
 test runthrough with monkey vs zookeeper
    0. get stats of monkey and zookeeper, 
        speed check, they tie with 25 speed so its a 50/50 chance each turn who goes first

    1. roll speed, monkey goes first 
        monkey chooses weapon,  zk chooses prayer
        roll if weapon hits, it hits so calc damage
        zk takes damage, rolls for prayer type and got patrick points (you see zk shudder)

    2. roll speed, zk goes first
        monkey chooses weapon, zk chooses dodge (priority)
        monkey did not choose status, so dodge fails
        monkey calc if it hits, yes hit

    3. roll speed, zk goes first
        monkey chooses weapon, zk chooses weapon
        monkey calc if it hits, yes hit so calc damage
        zk takes damage, calc if hits, yes hit so calc damage

    4. roll speed, zk goes first
        monkey chooses weapon, zk chooses prayer 
        zk rolls which prayer, gets heal, calc heal amount
        monkey rolls if weapon hits, it does, zk dies

 
 
 
 """ 



"""pa = 0.1
pb = 0.43
pc = 0.57875
pd = 0.95
pe = 1"""