
import numpy as np

class NumPyCreator:

	def from_list(self, nb):
		return np.array(nb)

	def from_tuple(self, nb):
		return np.array(nb)
	
	def from_shape(self, nb, value=0):
		return np.full(nb, value)

	def from_iterable(self, nb):
		return np.array(tuple(nb))
	
	def identity(self, nb):
		return np.eye(nb)
	
	def random(self, nb):
		return np.random.rand(nb[0], nb[1])


npc = NumPyCreator()
print (npc.from_list([[1, 2, 3], [4, 5, 6]]))
print (npc.from_tuple(("a","b","c")))
print (npc.from_shape((3, 5), 2))
print (npc.from_iterable(range(5)))
print (npc.identity(4))
print (npc.random((3,5)))