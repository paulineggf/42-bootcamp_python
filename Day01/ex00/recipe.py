
class Recipe:
    """Cette classe permet d'enregistrer une recette de cuisine"""

    objects = 0
    name = ""
    cooking_lvl = 0
    cooking_time = 0
    ingredients = []
    description = ""
    recipe_type = ""

    def __init__(self):
        Recipe.objects += 1
        pass

    def write(self, message):
        """Cette methode permet d'ecrire la description"""
        
        if self.description != "":
            self.description += '\n'
        self.description += message


    def recipe_print(self):
        """ Cette methode permet de lire la description"""

        print (self.name)
        print (self.cooking_lvl)
        print (self.cooking_time)
        print (self.ingredients)
        print (self.description)
        print (self.recipe_type)

    def delete(self):
        """Cette methode permet d'effacer la description"""

        self.description = ""


    def how_many(cls):
        """Cette methode de classe affiche le nombre d'objets crees"""

        print("{} created object(s)" .format(cls.objects))
    how_many = classmethod(how_many)


    def print_message():
        """Affiche quelque chose a l'ecran peu importe les donnees de l'objet"""

        print ("Affiche la meme chose dans tous les cas")
    print_message = staticmethod(print_message)

    def __str__(self):

        txt = self.name + ' ' + self.description
        return txt