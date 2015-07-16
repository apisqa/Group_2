"""Word-revert the string"""
s = raw_input('\nEnter the string to revert:\n')
temp = ''
result = ''
for i in range(1, len(s) + 1):
    temp2 = s[len(s) - i]
    if temp2 != ' ':
        temp = temp2 + temp
    else:
        result += temp + ' '
        temp = ''
result += temp
print('Final string is:\n%s' % result)