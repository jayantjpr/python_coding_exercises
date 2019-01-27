def mostCandy(k, j):
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
    print(max_chocklate)
    print(packet)

k = int(input())
j = input().split(sep=',')
mostCandy(k, j)

