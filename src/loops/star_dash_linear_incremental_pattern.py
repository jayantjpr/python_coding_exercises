n=int(input('enter number of rows: '))
for j in range(n):
	for i in range(j+1):
		if i % 2 == 0:
			print('*' , end='')
		else:
			print('_' , end='')
	print()
