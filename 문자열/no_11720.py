import sys

n=int(sys.stdin.readline())
digit=sys.stdin.readline().strip()

total=0
for i in range(n) :
    total+=int(digit[i])

print(total)