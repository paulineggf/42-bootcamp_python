
from dot import Dot
import numpy as np

def mat_vec_prod(x, y):
	array = []
	for i in range(0, len(x)):
		array2 = []
		array2.append(int((Dot(x[i],y))))
		array.append(array2)
	return np.array(array)


W = np.array([
    [ -8, 8, -6, 14, 14, -9, -4],
    [ 2, -11, -2, -11, 14, -2, 14],
    [-13, -2, -5, 3, -8, -4, 13],
    [ 2, 13, -14, -15, -14, -15, 13],
    [ 2, -1, 12, 3, -7, -3, -6]])

X = np.array([0, 15, -9, 7, 12, 3, -21]).reshape((7,1))
Y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((7,1))

print (mat_vec_prod(W,X))
print (mat_vec_prod(W,Y))
