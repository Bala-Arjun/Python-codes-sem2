filename = input("Enter the name of the file: ")
file = open(filename, 'r')
contents = file.read()
file.close()
lowercase_contents = contents.lower()

file = open(filename, 'w')
file.write(lowercase_contents)
file.close()

print(f"Contents of {filename} have been converted to lowercase.")
