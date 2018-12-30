n = int(input('Enter the number of rows required:'))
w = input('Which way want to print [Ascending ~ Descending]')

if w in 'Ascending':
    for i in range(1, n + 1):
        print((str(i) + ' ') * n)
else:
    for i in range(n, 0, -1):
        print((str(i) + ' ') * n)
