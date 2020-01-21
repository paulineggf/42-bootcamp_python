import sys

cookbook = {}
type(cookbook)

cookbook['sandwich'] = {
    'ingredients' : ['ham', 'bread', 'cheese', 'tomatoes'],
    'meal' : 'lunch',
    'prep_time' : '10'
}

cookbook['cake'] = {
    'ingredients' : ['flour', 'sugar', 'eggs'],
    'meal' : 'dessert',
    'prep_time' : '60'
}

cookbook['salad'] = {
    'ingredients' : ['avocado', 'arugula', 'tomatoes', 'spinach'],
    'meal' : 'lunch',
    'prep_time' : '15'
}

def print_cookbook(arg):
    i = 0
    for key in cookbook[arg]:
        print (key, ': ', end='')
        if key == 'ingredients':
            for key in cookbook[arg]['ingredients']:
                print (key, sep=' ', end='')
                i += 1
                if i != len(cookbook[arg]['ingredients']):
                    print (', ', end='')
                else:
                    print (' ', end='')
            print ()
        if key == 'meal':
            for key in cookbook[arg]['meal']:
                print (key, end='')
            print ()
        if key == 'prep_time':
            for key in cookbook[arg]['prep_time']:
                print (key, end='')
            print ()

def del_recipe(arg):
    del cookbook[arg]

if len(sys.argv) == 2 or len(sys.argv) == 3:
    if len(sys.argv) == 2:
        arg = str(sys.argv[1])
        if arg in cookbook:
            print_cookbook(arg)
        else:
            print ('This recipe doesn\'t exist')
    else:
        if str(sys.argv[1]) == 'delete':
            arg = str(sys.argv[2])
            if arg in cookbook:
                del_recipe(arg)
            else:
                print ('This recipe doesn\'t exist')
        else:
            print ('Try again')
else:
    print ('Try again')
