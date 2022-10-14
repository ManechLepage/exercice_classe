"""
Nom : Manech Lepage
Groupe : 403
Exercice 5 : Dataclass
"""

from dataclasses import dataclass
import random

@dataclass
class PlayerStats:
    """
    Class avec les statistiques d'un joueur
    """
    force: int
    dex: int
    con: int
    intelligence: int
    wis: int
    cha: int

player1 = PlayerStats(random.randint(1,20), random.randint(1,20), random.randint(1,20), random.randint(1,20), random.randint(1,20), random.randint(1,20))
print(player1.force, player1.dex, player1.con, player1.intelligence, player1.wis, player1.cha)