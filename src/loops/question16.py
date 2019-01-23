with open('16.txt') as f:
    print(f.read())

n = int(input('Enter the last number:'))
for i in range(1, n + 1):
    print( (str(i) + ' ') * ( n + 1 - i ) )
