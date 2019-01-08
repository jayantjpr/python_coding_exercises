with open("4.txt") as f:
	print(f.read())
with open("8.txt") as f:
	print(f.read())

w = input('Which one do you want to print?[4 or 8]')
n = ord(input('Enter the end character [A-Z]?'))

rows = n - ord('A') + 1
if w == '4':
    for j in range(rows):
        print((chr(ord('A') + j) + ' ') * rows)

elif w == '8':
    for i in range(rows, 0, -1):
        print((chr(64 + i) + ' ') * rows)

else:
	print('No such Pattern Exist')

