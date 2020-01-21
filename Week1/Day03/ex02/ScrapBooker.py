
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from imageprocessor import ImageProcessor

class ScrapBooker:

	def __init__(self):
		pass 

	def crop(self, array, dimensions, position=(0,0)):
		return array[position[0]:dimensions[0], position[1]:dimensions[1]]

	def thin(self, array, n, axis=0):
		return np.delete(array, slice(0, array.shape[int(axis)], n), axis)

	def juxtapose(self, array, n, axis):
		img = array
		for _ in range(1, n):
			img = np.concatenate((img, array), axis)
		return img

	def mosaic(self, array, dimensions):
		img = array
		for _ in range(1, dimensions[0]):
			img = np.concatenate((img, array), 0)
		img2 = img
		for _ in range(1, dimensions[1]):
			img2 = np.concatenate((img2, img), 1)
		return img2


img = ImageProcessor()
array = img.load('./42AI.png')
sb = ScrapBooker()
# img.display(sb.crop(array, (45,50)))
# img.display(sb.juxtapose(array, 4, 0))
img.display(sb.mosaic(array, (4, 2)))
