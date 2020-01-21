
def fahrenheit(T):
	return ((float(9) / 5 * T + 32))

def ft_map(function, lst):
	
	lst = list(lst)
	for i in range(0, len(lst)):
		lst[i] = function(lst[i])
	return lst

temperatures = (36.5, 37, 37.5, 38, 39)
temp2 = [36.5, 37]

print (ft_map(fahrenheit, temp2))
# print (list(ft_map(fahrenheit, temperatures)))
