import sys

n= int(sys.stdin.readline())

string=sys.stdin.read().strip().split()
cnt=0

before=''
for a in string :
    res=set()
    for i in a:
        if i not in res :
            res.update(i)
            before=i
        else :
            if before != i :
                res.remove(i)
                break;
            else :
                continue
    else :
        cnt+=1
print(cnt)
