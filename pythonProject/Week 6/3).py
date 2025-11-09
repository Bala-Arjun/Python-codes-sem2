l=list(map(str,input().split()))
count=0
count1=0
for i in range(0,len(l)):
    for j in range(0,len(l)):
        if l[j]==l[i]:
            count+=1
    count1+=1
    print(f"{l[i]}:{count}")
    count=0