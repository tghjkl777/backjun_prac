string=input()

count=[-1]*26

for i in string :
    num=ord(i)-97
    res=string.find(i)
    count[num]=res

count=list(map(str,count))
print(" ".join(count))
