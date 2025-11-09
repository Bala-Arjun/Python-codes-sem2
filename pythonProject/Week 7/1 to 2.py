source_file = input("Enter the name of the source file: ")
destination_file = input("Enter the name of the destination file: ")

file_in = open(source_file, 'r')
contents = file_in.read()
file_in.close()

file_out = open(destination_file, 'w')
file_out.write(contents)
file_out.close()

print("File copied successfully.")
