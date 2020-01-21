
class Vector:

	def __init__(self, value):
		self.values = []
		self.size = 0
		self.__check_value(value)

	def __check_value(self, value):
	
		if isinstance(value, list) == True:
			self.values = value
		elif isinstance(value, tuple) == True:
			self.__tuple_value(value)
		elif isinstance(value, int) == True:
			self.__int_value(value)
		self.size = len(self.values)

	def __tuple_value(self, value):

		for i in range(value[0], value[1]):
			self.values.append(float(i))
	
	def __int_value(self, value):

		for i in range(0, value):
			self.values.append(float(i))

	def __add__(self, other):

		values = []

		for i in range(0, len(self.values)):
			values.append(self.values[i] + float(other))
		return Vector(values)

	def __radd__(self, other):

		values = []

		for i in range(0, len(self.values)):
			values.append(self.values[i] + float(other))
		return Vector(values)

	def __mul__(self, other):

		values = []

		for i in range(0, len(self.values)):
			values.append(self.values[i] * float(other))
		return Vector(values)

	def __rmul__(self, other):

		values = []

		for i in range(0, len(self.values)):
			values.append(self.values[i] * float(other))
		return Vector(values)

	def __sub__(self, other):

		values = []

		for i in range(0, len(self.values)):
			values.append(self.values[i] - float(other))
		return Vector(values)

	def __truediv__(self, other):

		values = []
		
		for i in range(0, len(self.values)):
			values.append(self.values[i] / float(other))
		return Vector(values)

	def __rtruediv__(self, other):

		values = []
		
		for i in range(0, len(self.values)):
			values.append(self.values[i] / float(other))
		return Vector(values)		

	def __rsub__(self, other):

		values = []

		for i in range(0, len(self.values)):
			values.append(self.values[i] - float(other))
		return Vector(values)

	def __str__(self):

		return str(self.values) + str(self.size)

	def __repr__(self):

		return str(self.values) + str(self.size)	