
import numpy as np

def mean(x):
	result = 0
	for i in range(0, len(x)):
		result += x[i]
	return result / len(x)

# X = np.array([0, 15, -9, 7, 12, 3, -21])
# print (mean(X ** 2))