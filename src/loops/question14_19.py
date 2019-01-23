with open('14.txt') as f:
    print(f.read())

with open('19.txt') as f:
    print(f.read())


w = input('Which one do you want to print?[14 or 19]')
n = ord(input('Enter the end character'))
a = n - 64

if w == '14':
    for i in range (1, a + 1):
        for j in range(1,i+1):
            print( chr( 64 + j ) + ' ', end = '')
        print()

elif w == '19':
    for i in range(a, 0, -1):
        for j in range(1, i + 1):
            print( chr(64 + j) + ' ', end = '')
        print()

else:
    print('No such pattern exist')
