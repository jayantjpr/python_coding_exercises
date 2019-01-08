with open("2.txt") as f:
	print(f.read())
with open("6.txt") as f:
	print(f.read())

w = input('Which one do you want to print?[2 or 6]')
n = int(input('Enter the number of rows required:'))

if w == '2':
    for i in range(1, n + 1):
        print((str(i) + ' ') * n)
elif w == '6':
    for i in range(n, 0, -1):
        print((str(i) + ' ') * n)
else:
	print('No such Pattern Exist')
	


