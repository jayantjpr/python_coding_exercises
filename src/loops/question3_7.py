with open("3.txt") as f:
	print(f.read())
with open("7.txt") as f:
	print(f.read())

w = input('Which one do you want to print?[3 or 7]')
n = int(input('Enter starting number:'))
l = ''

if w == '3':
    for i in range(1, n + 1):
        l += str(i) + ' '

    for j in range(1, n + 1):
        print(l)

elif w == '7':
    for i in range(n, 0, -1):
        l += str(i) + ' '

    for j in range(n):
        print(l)
else:
	print('No such Pattern Exist')

