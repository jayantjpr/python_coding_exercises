def minimalTime(m,t):
    x = min(t) * (m - 1)
    for k in t:
        x = x + k
    return x

N = int(input())
for n in range(N):
    m = int(input())
    t = [int(x) for x in input().split(sep = ',')]
    print(minimalTime(m,t)) 

