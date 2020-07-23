import sys

string=sys.stdin.readline().strip()
cnt=0
while(string) :

    if string.find('c=') !=-1 :
        string= string.replace('c=',' ',1)
        cnt+=1
    elif string.find('c-') !=-1 :
        string= string.replace('c-',' ',1)
        cnt+=1
    elif string.find('dz=') !=-1 :
        string= string.replace('dz=',' ',1)
        cnt+=1
    elif string.find('d-') !=-1 :
        string= string.replace('d-',' ',1)
        cnt+=1
    elif  string.find('lj') !=-1 :
        string= string.replace('lj',' ',1)
        cnt+=1
    elif  string.find('nj') !=-1 :
        string = string.replace('nj', ' ',1)
        cnt+=1
    elif string.find('s=') !=-1 :
        string = string.replace('s=', ' ',1)
        cnt+=1
    elif string.find('z=') !=-1 :
        string = string.replace('z=', ' ',1)
        cnt+=1
    else :
        string=list(string.replace(" ",""))

        cnt += len(string)
        break;
print(cnt)
