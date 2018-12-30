n = int(input('Enter the end number:'))
w = input('Which way you want to print [Ascending ~ Descending]')

if w == 'Ascending':
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()
else:
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()
