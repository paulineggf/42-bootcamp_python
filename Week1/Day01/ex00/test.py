from book import Book
from recipe import Recipe

cookbook = Book()
cookbook.name = "cookbook"
print (cookbook.name)

quiche = Recipe()
quiche.name = "quiche"
quiche.cooking_lvl = 1
quiche.cooking_time = 30
quiche.ingredients = ['lardons', 'creme fraiche']
quiche.recipe_type = 'starter'
quiche.description = "Battre les lardons, les oeufs et la creme"

sandiwch = Recipe()
sandiwch.name = "sandiwch"
sandiwch.cooking_lvl = 2
sandiwch.cooking_time = 5
sandiwch.ingredients = ['jambon', 'fromage']
sandiwch.recipe_type = 'lunch'
sandiwch.description = "Mettre le jambon et le fromage dans le pain"


curry = Recipe()
curry.name = "curry"
curry.cooking_lvl = 2
curry.cooking_time = 5
curry.ingredients = ['riz', 'curry', 'poivrons']
curry.recipe_type = 'lunch'
curry.description = "Curry poivron"

print ('name:', quiche.name)

for i in quiche.ingredients:
	print ('ingredient:', i)

print ('level:', quiche.cooking_lvl)

cookbook.add_recipe(quiche)
cookbook.add_recipe(curry)
cookbook.add_recipe(sandiwch)
cookbook.add_recipe(10)
cookbook.get_recipes_by_types('starter')
cookbook.get_recipes_by_name("quiche")

print (str(quiche))
print (cookbook.creation_date)
print (cookbook.last_update)

print ('LUNCH')
cookbook.get_recipes_by_types('lunch')

print (str(curry))

cookbook.get_recipes_by_name("sandiwch")


