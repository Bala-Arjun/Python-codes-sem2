count=0
n=2
start=int(input())
end=int(input())
for i in range(start, end+1):
    for n in range(2, i-1):
        if i%n==0:
            count+=1
    if count==0:
        print(i)
    count=0
    n=2