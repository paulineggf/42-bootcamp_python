import datetime
from recipe import Recipe

class Book:
    """Livre de recettes"""
    
    name = ""
    last_update = datetime.datetime.now()
    creation_date = datetime.datetime.now()
    recipes_list = {    'starter' : [],
                        'lunch' : [],
                        'dessert' : [],
                        'unknown' : []
                    }

    def __init__(self):
        pass

    def get_recipes_by_types(self, recipe_type):
        for element in self.recipes_list[recipe_type]:
            element.recipe_print()

    def get_recipes_by_name(self, name):
        for element in self.recipes_list:
            for el in self.recipes_list[element]:
                if el.name == name:
                    print ('Name:', el.name)
        
    def add_recipe(self, recipe):
        if isinstance(recipe, Recipe) == True:       
            if recipe not in self.recipes_list:
                self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.datetime.now()
        else:
            print ('ERROR')