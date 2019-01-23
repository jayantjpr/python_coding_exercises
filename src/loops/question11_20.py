with open("11.txt") as f:
	print(f.read())
with open("20.txt") as f:
	print(f.read())

	
w = input('Which one do you want to print?[11 or 20]')
n = int(input('Enter the end numer:'))

if w == '11':
    for i in range(1, n + 1):
        print(i * (str(i) + ' '))
elif w == '20':
    for i in range(n, 0, -1):
        print(i * (str(i) + ' '))
else:
	print('No such Pattern Exist')

