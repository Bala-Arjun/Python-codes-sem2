infile = open("text", "r")
count = 0
word=0
c=0
while True:
    line = infile.readline()
    lw=line.split(" ")
    for i in lw:
        c+=len(i)
    if line == '':
        break
    if line.strip() == '':
        break
    word=word+len(lw)
    count += 1
print(f"No of lines: {count}")
print(f"No of words: {word}")
print(f"No of characters: {c}")
infile.close()
