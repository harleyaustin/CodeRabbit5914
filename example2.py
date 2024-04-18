# Open the file in read mode
with open('test.txt', 'r') as file:
    # Read the content of the file
    content = file.read()

# Replace all occurrences of 'a' with 'b'
content = content.replace('a', 'b')

# Open the file in write mode and write the modified content
with open('test.txt', 'w') as file:
    file.write(content)

print("Replacement done successfully!")
