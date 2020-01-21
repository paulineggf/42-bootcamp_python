
import numpy as np

def dot(x, y):
	result = 0
	for i in range(0, len(x)):
		result += x[i] * y[i]
	return float(result)

X = np.array([0, 15, -9, 7, 12, 3, -21])
Y = np.array([2, 14, -13, 5, 12, 4, -19])

print (dot(Y, Y))