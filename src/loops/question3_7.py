n = int(input('Enter starting number:'))
w = input('Which way you want to print [Ascending ~ Descending]')
l = ''

if w == 'Ascending':
    for i in range(1, n + 1):
        l += str(i) + ' '

    for j in range(1, n + 1):
        print(l)

else:
    for i in range(n, 0, -1):
        l += str(i) + ' '

    for j in range(n):
        print(l)
