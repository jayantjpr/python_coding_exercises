with open("1.txt") as f:
	print(f.read())
n = int(input('Enter the number of rows required:'))
for i in range(0, n):
    print('* ' * n)
