filename = input("Enter the name of the file: ")
file = open(filename, 'r')
contents = file.read()
file.close()
uppercase_contents = contents.upper()

file = open(filename, 'w')
file.write(uppercase_contents)
file.close()

print(f"Contents of {filename} have been converted to uppercase.")
