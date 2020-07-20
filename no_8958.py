import sys

n=int(sys.stdin.readline())
scores=list(sys.stdin.read().split())

for i in range(n) :
    score_sum = 0
    before = 0
    for j in scores[i]:
        if j=='X' :
            before=0
        else :
            before+=1
            score_sum+=before
    print(score_sum)
