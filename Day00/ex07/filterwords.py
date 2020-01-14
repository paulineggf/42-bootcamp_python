import sys
import string

def split(s, nb):
   for c in s:
       if c in string.punctuation:
           s = s.replace(c, '') 
   s = s.split()
   len_s = len(s) - 1
   for i in range(len_s, -1, -1):
       if len(s[i]) < nb:
            del s[i]
   print (s)

def error():
    print ('ERROR')

if len(sys.argv) == 3:
    try:
        nb = int(sys.argv[2])
        s = str(sys.argv[1])
        split(s, nb)
    except ValueError:
        error()
else:
    error()
