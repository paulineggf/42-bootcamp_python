import sys

def up_low(c):
    if (c.isupper()) == True:
        print (c.lower(), end="")
    elif (c.islower()) == True:
        print (c.upper(), end="")

argv_len = len(sys.argv) - 1
if argv_len > 1:
    while argv_len >= 1:
        a = sys.argv[argv_len]
        i = len(a) - 1
        while i >= 0:
            up_low(a[i])
            i -= 1 
        if argv_len > 1:
            print (" ", end="")
        argv_len -= 1
    print ("\n", end="")
else:
    sys.exit()
