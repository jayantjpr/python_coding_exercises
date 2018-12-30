n = ord(input('Enter the end character [A-Z]?'))
w = input('Which way you want to print [Ascending ~ Descending]')
rows = n - ord('A') + 1
if w == 'Ascending':
    for j in range(rows):
        print((chr(ord('A') + j) + ' ') * rows)

else:
    for i in range(rows, 0, -1):
        print((chr(64 + i) + ' ') * rows)
