with open("12.txt") as f:
	print(f.read())
with open("17.txt") as f:
	print(f.read())

w = input('Which one do you want to print?[12 or 17]')
n = int(input('Enter the end number:'))

if w == '12':
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()
elif w == '17':
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

else:
	print('No such Pattern Exist')
	
