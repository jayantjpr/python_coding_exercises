with open("10.txt") as f:
	print(f.read())
with open("15.txt") as f:
	print(f.read())

w = input('Which one do you want to print?[10 or 15]')
n = int(input('Number of rows to be printed:'))

if w == '10':
    for i in range(1, n + 1):
        print('* ' * i)

elif w == '15':
    for i in range(n, 0, -1):
        print('* ' * i)

else:
	print('No such Pattern Exist')



