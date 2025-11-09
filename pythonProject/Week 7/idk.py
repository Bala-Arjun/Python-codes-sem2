filename = input("Enter the name of the file: ")
file = open(filename, 'r')
contents = file.read()
file.close()

words = contents.split()
unique_words = set(words)
sorted_words = sorted(unique_words)

for word in sorted_words:
    print(word)
