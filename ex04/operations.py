import sys

def operation(val1, val2):
    print ("Sum:", val1 + val2)
    print ("Difference:", val1 - val2)
    print ("Product:", val1 * val2)
    if val2 != 0:
        print ("Quotient:", val1 / val2)
        print ("Reminder:", val1 % val2)
    else:
        print ("ERROR (div by zero)")
        print ("ERROR (modulo by zero)")

if len(sys.argv) == 3:
    try:
        val1 = int(sys.argv[1])
        val2 = int(sys.argv[2])
        operation(val1, val2)
    except ValueError:
        print ("InputError: only numbers")
        print ("Usage: python operations.py\nExample:\n\tpython operations.py 10 3")
elif len(sys.argv) > 3:
    print ("InputError: too many arguments")
    print ("Usage: python operations.py\nExample:\n\tpython operations.py 10 3")
