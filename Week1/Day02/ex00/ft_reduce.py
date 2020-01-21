
def	do_sum(x1, x2):
	return x1 + x2

def ft_reduce(function, lst):

	result = 0
	lst = list(lst)
	for i in range(0, len(lst)):
		result = function(result, lst[i])
	return result

result = ft_reduce(do_sum, range(1, 5))
print (result)
