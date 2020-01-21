
result = 0
l1 = ["eat","sleep","repeat"]
for count,ele in enumerate(l1,0): 
    result += count * len(ele)
print (result)

result = 0
words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]

for el,count in zip(words, coefs):
	result += count * len(el)
print (result)