from random import randint


def gen(n, x, y):
    return [randint(x, y) for z in range(n)]


def find(summ, l):
    for elem in l:
        search_for = summ - elem
        if search_for > 0 and search_for in l:
            print(str(elem) + ' + ' + str(search_for) + ' = ' + summ)


summ = 5
l = gen(10, 1, 10)
l1 = sorted(l)
left = 0
right = len(l)

while(left < right):
    result = l1[left] + l1[right]
    if summ == result:
        print('\n%s + %s equals %s' % (l1[left], l1[right], summ))
        left += 1
        right -= 1
    elif summ < result:
        left += 1
    else:
        right += 1