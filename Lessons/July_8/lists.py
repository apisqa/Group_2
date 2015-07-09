l = [5, 4, 6, 4]

print('Initial list: %s' % l)
l.append(7)

print('After append: %s' % l)

l.extend('g')
print('After extend: %s' % l)

print('Here are %s "4s"' % l.count(4))