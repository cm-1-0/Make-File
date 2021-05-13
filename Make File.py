message = input("Enter the message: ")

with open("Testing_File", "w") as new_file:
    new_file.write(message)
