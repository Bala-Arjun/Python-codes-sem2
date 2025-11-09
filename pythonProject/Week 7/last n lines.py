filename = input("Enter file name: ")
n = int(input("Enter the number of lines to read from the end: "))
file = open(filename, 'r')
lines = file.readlines()
file.close()
for line in lines[-n:]:
    print(line, end='')
