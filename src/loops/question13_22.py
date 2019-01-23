with open('13.txt') as f:
    print(f.read())

with open('22.txt') as f:
    print(f.read())

w = input('which one do you want to print?[13 or 22]')
n = ord(input('Enter the end character:'))

if w == '13':
    for i in range(1, n - 63):
        print( (chr( 64 + i ) + ' ') * i )

elif w == '22':
    for i in range(n - 64, 0, -1):
        print( (chr( 64 + i ) + ' ') * i )

else:
    print('No such pattern exist.')
