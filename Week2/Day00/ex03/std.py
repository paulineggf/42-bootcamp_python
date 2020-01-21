
from variance import variance
import numpy as np

def std(x):
	return (np.sqrt(variance(x)))

x = np.array([0, 15, -9, 7, 12, 3, -21])
print (std(x))
y = np.array([2, 14, -13, 5, 12, 4, -19])
print (std(y))