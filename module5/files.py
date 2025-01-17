"""Operations for writing and appending to files."""
# Create a new file
opfile = open("output.txt", 'w')
# Writing to the file
opfile.write("Writing to a new file.")
# To add another line the newline character must be used
opfile.write("\nSecond line.")
# Ensure changes are saved by closing the file
opfile.close()
# Read and display the contents of the file
infile = open("output.txt")
print("\nRead the original file:\n")
print(infile.read())
infile.close()
# Reopen the file in append mode to add to the file
opfile = open("output.txt", 'a')
# Note the use of newline characters
opfile.write("\nAdding to the file.")
opfile.write("\nAdding another line.")
# Ensure changes are saved by closing the file
opfile.close()
# Read and display the contents of the modified file
infile = open("output.txt")
print("\nRead the modified file:\n")
print(infile.read())
infile.close()