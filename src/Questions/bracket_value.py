i = input('Input the bracket pattern:')
index = 0
k = 0
a = 0
for r in i:
    if r == '(':
        a += 1
    elif r == ')':
        if i[index] == i[index - 1]:
            a -= 1
        else:
            k += (2 ** (a - 1))
            a -=1
    index += 1
print(k)
