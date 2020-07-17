import sys

my_mod=set()
num=sys.stdin.read().split()
int_num=list(map(int,num))

for i in int_num :
    my_mod.add(i%42)

print(len(my_mod))

