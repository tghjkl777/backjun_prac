import sys

n=int(sys.stdin.readline())
string=[]
for i in range(n) :
    str=""
    a,b= sys.stdin.readline().split()
    a=int(a)
    for item in b :
        str=str+item*a
    string.append(str)

for i in string :
    print(i)