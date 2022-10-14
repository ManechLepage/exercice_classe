"""
Nom : Manech Lepage
Groupe : 403
Exercice 4 : Creation d'une classe Hero
"""
import random


class Hero:

    def __init__(self, name):
        self.hp = random.randint(1, 10) + random.randint(1, 10)
        self.attack = random.randint(1, 6)
        self.defense = random.randint(1, 6)
        self.name = name

    def attack(self):
        return random.randint(1, 6) + self.attack

    def take_dammage(self, dammage):
        self.hp -= dammage - self.defense

    def is_alive(self):
        if self.hp > 0 :
            return True
        else :
            return False

