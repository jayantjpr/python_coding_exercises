with open('21.txt') as f:
    print(f.read())

n = int(input('Enter the last number:'))
k = 0
for i in range(n, 0, -1):
   while k <= n:
       for j in range(n, k, -1):
           print( str(j), end = ' ')
       k += 1
       print()

