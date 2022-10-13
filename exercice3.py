"""
Nom : Manech Lepage
Groupe : 403
Exercice 3 : Classe cercle
"""
from math import pi


class Cercle:
    """
    classe qui permet de creer un cercle avec le rayon
    """
    def __init__(self, radius):
        """
        fonction appeler lors de la creation dun instance qui cree les attributs
        :param radius: rayon du cercle
        """
        self.radius = radius
        self.area = None
        self.circumference = None

    def calcul_aire(self):
        """
        fonction qui permet de calculer l'aire du cercle
        :return: l'aire du cercle arrondis au centieme
        """
        self.area = pi * self.radius ** 2
        return round(self.area, 2)

    def calcul_circonference(self):
        """
        fonction qui permet de calculer la circonference du cercle
        :return: la circonference du cercle arrondis au centieme
        """
        self.circumference = 2 * pi * self.radius
        return round(self.circumference, 2)


cercle1 = Cercle(8)
print(f"Aire du cercle : {cercle1.calcul_aire()}")
print(f"Circonference du cercle : {cercle1.calcul_circonference()}")
