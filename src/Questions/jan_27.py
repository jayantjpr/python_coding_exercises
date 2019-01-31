#Question : https://community.topcoder.com/stat?c=problem_statement&pm=15289

def copy(j):
    a =[]
    s = [-1,-1,-1,-1,4]
    for i in range(5):
        a.append(j[i] + s[i],)
    return a

N = int(input())
for n in range(N):
    j = [int(x) for x in input().split(sep = ',')]
    print(copy(j))


