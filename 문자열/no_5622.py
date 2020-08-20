import sys

num_s=sys.stdin.readline().strip()
num=list(num_s)

sec=0
for i in num :
    if ord('A')<=ord(i)<=ord('C') :
        sec+=3
    elif ord('D')<=ord(i)<=ord('F') :
        sec+=4
    elif ord('G')<=ord(i)<=ord('I') :
        sec+=5
    elif ord('J')<=ord(i)<=ord('L') :
        sec+=6
    elif ord('M')<=ord(i)<=ord('O') :
        sec+=7
    elif ord('P')<=ord(i)<=ord('S') :
        sec+=8
    elif ord('T')<=ord(i)<=ord('V') :
        sec+=9
    elif ord('W')<=ord(i)<=ord('z') :
        sec+=10
    else :
        continue

print(sec)