
import numpy as np
from Mean import mean

def mse(y, y_hat):
	result = 0
	for i in range(0, len(y)):
		result += (y[i] - y_hat[i]) ** 2
	return result / len(y)


Y = np.array([0, 15, -9, 7, 12, 3, -21])
Y_HAT = np.array([2, 14, -13, 5, 12, 4, -19])

print (mse(Y, Y_HAT))

"""Computes the mean squared error of two non-empty numpy.ndarray, using
a for-loop. The two arrays must have the same dimensions.
    Args:
     y: has to be an numpy.ndarray, a vector.
     y_hat: has to be an numpy.ndarray, a vector.
    Returns:
     The mean squared error of the two vectors as a float.
     None if y or y_hat are empty numpy.ndarray.
     None if y and y_hat does not share the same dimensions.
    Raises:
     This function should not raise any Exception.
"""