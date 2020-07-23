import sys

string=sys.stdin.readline().strip()
string=string.upper()

cnt=-1

for i in string :
    if string.count(i)> cnt :
        cnt=string.count(i)
        res=i
    elif string.count(i)==cnt:
        res="?"
    else :
        continue
    string=string.replace(i, "")

print(res)