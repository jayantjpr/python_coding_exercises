# Question : https://community.topcoder.com/stat?c=problem_statement&pm=15095

def getShownPostTime(currentTime, postTime):
    h = currentTime[0] - postTime[0]
    m = currentTime[1] - postTime[1]
    s = currentTime[2] - postTime[2]

    if s < 0:
        s += 60
        m -= 1
    if m < 0:
        m += 60
        h -=1
    if h < 0:
        h += 24
    
    if h != 0:
        return "{} hours ago.".format(h)
    elif m != 0:
        return "{} minutes ago.".format(m)
    else:
        return "few seconds ago."

N = int(input())
for n in range(N):
    currentTime = [int(x) for x in input().split(sep = ':')]
    postTime = [int(x) for x in input().split(sep = ':')]
    print( getShownPostTime (currentTime, postTime))
