import sys

s = sys.argv[1].lstrip('-+').isdigit()
if len(sys.argv) == 2 and s == True:
    if int(sys.argv[1]) == 0:
        print ("I'm zero.")
    elif int(sys.argv[1]) % 2 == 0:
        print ("I'm Even.")
    else:
        print ("I'm Odd.")
else:
    print ("ERROR")
