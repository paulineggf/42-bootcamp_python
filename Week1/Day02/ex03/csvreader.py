
class CsvReader():

	def __init__(self, filename="", sep=',', header=False, skip_top=0, skip_bottom=0):
		self.filename = filename
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom
		self.file = None
		
	def __enter__(self):
		print('test1')
		print (self.filename)
		self.file = open(self.filename, 'r')
		return self

	def __exit__(self, file, value, traceback):
		self.file.close()

	def getdata(self):
		print ('getdata')
		contents = self.file.read()
		print (contents)

	def getheader(self):
		print ('getheader')

if __name__ == "__main__":
	# with CsvReader('good.csv') as file:
		# data = file.getdata()
		# header = file.getheader()
	# with CsvReader('good.csv') as file:
	# 	if file == None:
	# 		print ("File is corrupted")

	with CsvReader('good.csv') as file:
		file.getdata()
	# file = []
	# for x in range(100):
	# 	file.append(open('good.csv', 'r'))
	# print (file)