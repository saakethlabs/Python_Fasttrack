# Open a file for writing
file = open("example.txt", "w")

# Write some text
file.write("Hello, world!\n")
file.write("This is a new line of text.")

# Close the file to save changes
file.close()


# Reading
file = open("example.txt", "r")
content = file.read()  # Reads the entire file as a single string
print(content)
file.close()

# Reading line by line
file = open("example.txt", "r")

for line in file:
    print(line.strip())  # Remove trailing newline characters

file.close()

# Append Mode
with open("saakethlabs.txt", "a") as file:
    file.write("\nThis line was added later.")

