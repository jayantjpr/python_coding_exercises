with open('23.txt') as f:
    print(f.read())

n = ord(input('Enter the end character:'))
a = n - 64
k = 0
for i in range(a, 0, -1):
    while k <= a:
        for j in range(a, k, -1):
            print(chr(64 + j), end=' ')
        k += 1
        print()
