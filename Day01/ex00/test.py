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

print ('name:', quiche.name)

for i in quiche.ingredients:
	print ('ingredient:', i)

print ('level:', quiche.cooking_lvl)

cookbook.add_recipe(quiche)
cookbook.add_recipe(10)


cookbook.get_recipes_by_types('starter')

cookbook.get_recipes_by_name("quiche")

print (str(quiche))
print (cookbook.creation_date)
print (cookbook.last_update)