a = [1, 2, 10, '.', '#', 3, 'A', 'a', 'ADFADFDF']

a.sort()

print(a)


l = range(1,11)
l1 = []
for i in range(len(l)):
    temp = l[i]*2
    print temp
    l1.append(temp)

l1.reverse()
print l1

while 4 in l1:
    l1.remove(4)

del l1[3]

l1.sort()
l1.append("Stan")

print l1