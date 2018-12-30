n = int(input('Enter the end numer:'))
w = input('Which way you want to print [Ascending ~ Descending]')
if w == 'Ascending':
    for i in range(1, n + 1):
        print(i * (str(i) + ' '))
elif w == 'Descending':
    for i in range(n, 0, -1):
        print(i * (str(i) + ' '))
