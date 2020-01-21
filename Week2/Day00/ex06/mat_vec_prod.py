
from dot import Dot
import numpy as np

def Mat_vec_prod(x, y):
	array = []
	for i in range(0, len(x)):
		array2 = []
		array2.append(int((Dot(x[i],y))))
		array.append(array2)
	return np.array(array)
