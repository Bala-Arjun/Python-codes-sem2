if __name__ == '__main__':
    idk=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        idk.append(name)
        idk.append(score)
    idk.sort()
    count=0
    i=3
    while True:
        if idk[3]==idk[i+2]:
            i+=2
            count+=1
        else:
            break
    for j in range (count):
        print(idk[2*count])