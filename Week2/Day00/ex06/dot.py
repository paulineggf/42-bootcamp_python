
import numpy as np

def Dot(x, y):
	result = 0
	for i in range(0, len(x)):
		result += x[i] * y[i]
	return float(result)
