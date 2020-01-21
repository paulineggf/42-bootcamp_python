
import numpy as np
from Mean import mean

def variance(x):
	return mean((x - mean(x)) ** 2)
