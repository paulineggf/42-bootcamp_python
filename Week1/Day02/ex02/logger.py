
import time
import logging
from random import randint

class CoffeeMachine():
	water_level = 100
	
	def log(funct):
		logging.basicConfig(filename='machine.log', format='(%(name)s) %(message)s', level=logging.INFO)
		def wrapper(*args, **kwargs):
			t = time.time()
			value = funct(*args, **kwargs)
			t = round(time.time() - t, 3)
			logging.info("Running:  %s       [ exec-time = %.3f ms ]" % (funct.__name__.replace('_', ' ').title(), t))
			return value
		return wrapper

	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
			return False
	
	@log
	def boil_water(self):
		return "boiling..."
	
	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")
	
	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")

if __name__ == "__main__":
	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()
	machine.make_coffee()
	machine.add_water(70)