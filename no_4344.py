import sys

test_case= int(sys.stdin.readline())
test_list= list(map(int,sys.stdin.read().split()))

res_list=[]
cnt_list=[]
for i in range(test_case):
    cnt=0

    if i==0:
        start=0
        end=start+test_list[start]
        # res_list.append(sum(test_list[start+1 :end+1])/test_list[start])
        avg=sum(test_list[start+1 :end+1])/test_list[start]
        for i in range(start+1,end+1) :
            if avg < test_list[i] :
                cnt+=1
        res_list.append(cnt/test_list[start]*100)
        cnt_list.append(cnt)
        start=end+1
    else:
        end=start+test_list[start]
        # res_list.append(sum(test_list[start+1 :end+1])/test_list[start])

        avg=sum(test_list[start+1 :end+1])/test_list[start]
        for i in range(start+1,end+1) :
            if avg < test_list[i] :
                cnt+=1
        res_list.append(cnt/test_list[start]*100)
        cnt_list.append(cnt)
        start=end+1

for i in res_list :
    print("%.3f" %i,"%",sep="")

