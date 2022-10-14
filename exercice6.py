"""
Nom : Manech Lepage
Groupe : 403
Exercice 6 : Hero avec dataclass
"""
from dataclasses import dataclass
import random

@dataclass
class PlayerStats:
    """
    Class avec les statistiques d'un joueur
    """
    attack: int
    hp: int
    defense: int

class Hero:

    def __init__(self, name):
        """
        fonction qui creer les statistiques du joueur
        :name: nom du joueur
        """
        self.stats = PlayerStats(random.randint(1, 6), random.randint(1, 10) + random.randint(1, 10), random.randint(1, 6))
        self.name = name

    def attack(self):
        """
        fonction qui retourne une attaque
        :return: le dommage de l'attaque
        """
        return random.randint(1, 6) + self.stats.attack

    def take_dammage(self, dammage):
        """
        fonction qui change le nombre de vie apres une attaque
        :dammage: nombre de dommage que le joueur recois
        """
        self.stats.hp -= dammage - self.stats.defense

    def is_alive(self):
        """
        fonction qui retourne une bool qui dit si le joueur est vivant ou non
        :return: joueur est vivant ou non
        """
        if self.stats.hp > 0 :
            return True
        else :
            return False
