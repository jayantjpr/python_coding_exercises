n = int(input('Number of rows to be printed:'))
w = input('[Ascending ~ Descending]?')
if w == 'Ascending':
    for i in range(1,n+1):
        print('*' * i)
else:
    for i in range(n,0,-1):
        print('*' * i)
