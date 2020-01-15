
def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(alphabet in vowels):
        return True
    else:
        return False

def ft_filter(function, lst):

	lst = list(lst)
	for i in range(len(lst) - 1, 0, -1):
		if function(lst[i]) == False:
			del lst[i]
	return lst

alphabet = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

filtered = ft_filter(filterVowels, alphabet)
print (filtered)