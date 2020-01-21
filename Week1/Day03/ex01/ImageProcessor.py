
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

class ImageProcessor:

	def __init__(self):
		pass

	def load(self, path=""):
		image = mpimg.imread(path)
		print (image.shape)
		return image

	def display(self, array):
		imgplot = plt.imshow(array)
		plt.show()

img = ImageProcessor()
array = img.load('./42AI.png')
img.display(array)