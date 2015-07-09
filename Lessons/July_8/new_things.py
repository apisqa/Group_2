"""raw_input vs input"""

"""
a = input('a:')
b = raw_input('b:')


print(a + 'X')
print(b + 'X')
print(int(b) + 6)
"""

"""try except"""
"""
try:
    a = input('d')
except NameError:
    print('WRONG')
"""

"""check for int"""
"""
d = ''
while not d.isdigit():
    d = raw_input('asd')
    try:
        int(d)
    except ValueError:
        print('Wrong, again')
"""