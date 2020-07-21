a = [
    [1,3],
    [5,3],
    [2,4]
]
one = [i for i in range(6)]


for i in range(len(a)): #  a 원소 순회
    if a[i][0] < a[i][1]:
        one[a[i][1]] = one[a[i][0]]
    else:
        one[a[i][0]] = one[a[i][1]]


# set 개수만큼 방을 만들어서 집어넣는 방법
answer = []
cnt = -1
for _ in range(len(set(one))):
    arr = []
    cnt+=1
    for idx,val in enumerate(one):
#         print(arr)
        temp = list(set(one))[cnt]
        if val == temp:
            arr.append(idx)
        else :
            continue;
    answer.append(arr)
print(answer, cnt)


