"""
Nom : Manech Lepage
Groupe : 403
Exercice 4 : Creation d'une classe Hero
"""
import random


class Hero:

    def __init__(self, name):
        """
        fonction qui creer les statistiques du joueur
        :name: nom du joueur
        """
        self.hp = random.randint(1, 10) + random.randint(1, 10)
        self.attack = random.randint(1, 6)
        self.defense = random.randint(1, 6)
        self.name = name

    def attack(self):
        """
        fonction qui retourne une attaque
        :return: le dommage de l'attaque
        """
        return random.randint(1, 6) + self.attack

    def take_dammage(self, dammage):
        """
        fonction qui change le nombre de vie apres une attaque
        :dammage: nombre de dommage que le joueur recois
        """
        self.hp -= dammage - self.defense

    def is_alive(self):
        """
        fonction qui retourne une bool qui dit si le joueur est vivant ou non
        :return: joueur est vivant ou non
        """
        if self.hp > 0 :
            return True
        else :
            return False

