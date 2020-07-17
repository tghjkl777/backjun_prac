import sys

n=int(sys.stdin.readline())

now_score=list(map(int,sys.stdin.readline().split()))

new_score=[]
for i in range(len(now_score)):
    new_score.append(now_score[i]/max(now_score)*100)

print(sum(new_score)/len(new_score))