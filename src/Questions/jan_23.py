# Question: https://www.topcoder.com/stat?c=problem_statement&pm=1521 
# To run: $python3 jan_23.py < jan_23_in.txt

def mostCandy(K, candy):
    max_candy = 0
    for candy_count in candy:
        max_candy = max(candy_count // (K+1) + candy_count % (K+1), max_candy)
    return max_candy

N = int(input()) # The number of test cases
for n in range(0, N):
    K = int(input())
    candy = [int(x) for x in input().split(sep=',')]
    print(mostCandy(K, candy))
