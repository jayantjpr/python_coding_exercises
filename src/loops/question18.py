with open('18.txt') as f:
    print(f.read())

n = ord(input('Enter the end character:'))
a = n - 63

for i in range(1, a + 1):
    print((chr( 64 + i ) + ' ') * (a - i))
