def canItBeDone(a, n):
    b = (n * (n + 1))/2
    if a >= b:
        return "possible"
    else:
        for i in range(a):
            if (i * (i + 1))//2 <= a:
                s = i
            break
        if n <= s:
            return "possible"
        else:
            return "impossible"
a = int(input())
n = int(input())
print(canItBeDone(a, n))
