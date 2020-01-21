
import numpy as np

def sum_(x, f):
	result = 0
	if len(x) == 0:
		return None
	for i in range(0, len(x)):
		result += float(f(x[i]))
	return result

X = np.array([0, 15, -9, 7, 12, 3, -21])
print (sum_([], lambda x:x))