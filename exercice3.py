"""
Nom : Manech Lepage
Groupe : 403
Exercice 3 : Classe cercle
"""
from math import pi


class Cercle:

    def __init__(self, radius):
        self.radius = radius
        self.area = None
        self.circumference = None

    def calcul_aire(self):
        self.area = pi * self.radius ** 2
        return round(self.area, 2)

    def calcul_circonference(self):
        self.circumference = 2 * pi * self.radius
        return round(self.circumference, 2)


cercle1 = Cercle(8)
print(f"Aire du cercle : {cercle1.calcul_aire()}")
print(f"Circonference du cercle : {cercle1.calcul_circonference()}")
