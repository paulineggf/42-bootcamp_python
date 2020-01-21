
import numpy as np
from Mean import mean

def variance(x):
	return mean((x - mean(x)) ** 2)


x = np.array([0, 15, -9, 7, 12, 3, -21])
print (variance(x))