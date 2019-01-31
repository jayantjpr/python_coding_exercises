# Question : https://community.topcoder.com/stat?c=problem_statement&pm=15274

def howMany(r2,r3,r5):
    for i in range(1,31):
        if i % 2 == r2 and i % 3 == r3 and i % 5 == r5:
            return i
N = int(input())
for n in range(N):
    r2 = int(input())
    r3 = int(input())
    r5 = int(input())
    print(howMany(r2,r3,r5))

