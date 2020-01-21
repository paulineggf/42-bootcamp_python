import datetime

def generator(text, sep=" ", option=None):

	s = []
	unique_list = []

	if isinstance(text, str) == False:
		return ("Error")
	s = text.split(sep)
	if (option == "shuffle"):
		while len(s) > 0:
			ret = (datetime.datetime.now().microsecond + 0) % len(s)
			el = s[ret]
			del s[ret]
			yield el
	elif (option == "ordered"):
		s = sorted(s)
		for i in s:
			yield i
	elif (option == "unique"):
		for i in s:
			if i not in unique_list:
				unique_list.append(i)
				yield i
	else:
		for i in s:
			yield i

for s in generator("hello test ca va hello ca va bien bonjour hola bla bla toto titi"):
	print ('ret', s)