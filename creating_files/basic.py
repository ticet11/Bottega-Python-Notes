# Will overwrite the current file
file_builder = open('logger.txt', 'w+')

for i in range(100):
    file_builder.write(f"I'm on line {i + 1}\n")

# file_builder.write('Hey, this is definitely a file')

file_builder.close()