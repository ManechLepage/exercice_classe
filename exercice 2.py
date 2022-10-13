"""
Nom : Manech Lepage
Groupe : 403
Exercice 2 : fonction rectangle
"""


class Rectangle:
    """
    classe qui permet de generer un rectanle et de calculer son aire
    """
    def __init__(self, width, height):
        """
        fonction appeler lors de la creation d'un instance de cette classe
        :param width: la largeur du rectangle
        :param height: la longueur du rectangle
        """
        self.width = width
        self.height = height
        self.area = None

    def calcul_aire(self):
        """
        fonction qui permet de calculer laire du rectangle
        :return: none
        """
        self.area = self.width * self.height

    def afficher_info(self):
        """
        fonction pour afficher les mesures du rectangle
        :return: la largeur, la longueur et l'aire
        """
        return self.width, self.height, self.area


rect1 = Rectangle(10, 15)
rect1.calcul_aire()
print(rect1.afficher_info())
