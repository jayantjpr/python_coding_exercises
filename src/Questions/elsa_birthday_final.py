k = int(input('Enter the number of students excluding Elsa:'))
j = input('Enter the packet sizes available in store:').split(sep=',')
max_chocklate = 0
packet = 0
for i in j:
    if int(i) < (k + 1):
        if int(i) > max_chocklate:
            max_chocklate = int(i)
            packet = int(i)
    elif int(i) > (k + 1): 
        d = int(i) // (k + 1)
        s = int(i) % (k + 1)
        if (d + s) > max_chocklate:
            max_chocklate = d + s
            packet = int(i)
print('Max chocklates she can have: {}'.format(max_chocklate))
print('She should choose packet with: {}'.format(packet))
