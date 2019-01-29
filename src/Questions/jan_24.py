# Question: https://www.topcoder.com/stat?c=problem_statement&pm=14664 
# To run: $python3 jan_24.py < jan_24_in.txt

def canItBeDone(pl, p):
    if pl >= sumTillN(p): 
        return "possible"
    else:
        return "impossible"

def sumTillN(n):
    return (n * (n + 1)) / 2;

N = int(input()) # The number of test cases
for n in range(N):
    pl = int(input())
    p = int(input())
    print(canItBeDone(pl, p))
