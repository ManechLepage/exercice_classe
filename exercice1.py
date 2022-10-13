"""
Nom : Manech Lepage
Groupe : 403
Exercice 1 : classe StringFoo
"""


class StringFoo:
    """
    classe qui permet de definir une string et de limprimer avec une autre fonction
    """

    def __init__(self):
        """
        fonction appeler quand une instance de la classe est creer
        """
        self.message = ""

    def set_string(self, message):
        """
        fonction qui definit self.message
        :param message: string qui peut etre imprimer avec print_string()
        :return: none
        """
        self.message = message

    def print_string(self):
        """
        fonction pour imprimer self.message
        :return: none
        """
        print(self.message.upper())


stringFoo = StringFoo()
stringFoo.set_string("moche")
stringFoo.print_string()
