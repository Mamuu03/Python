try:
# Open the file in write mode ('w')
    with open("my_file.txt", "w") as file:
        file.write("This is my text file in write mode\n")
        file.write("You can write anything numbers or strings\n")
        file.write("Counting numbers 123. Alphabetical letters ABC.\n")
    print("File successfully created!")

# Open the file in append mode ('a')
    with open("my_file.txt", "a") as file:
    # Append three additional lines of text to the existing content
        file.write("This is an append mode.\n")
        file.write("I have added 3 more lines to my previous file\n")
        file.write("Now I have a total of 6 lines. Lets see the output\n")
    print("File appended successfully.")

# Open the file in read mode ('r')
    with open("my_file.txt", "r") as file:
    # Read and display the contents of the file
       contents = file.read()
       print(contents)

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("Permission denied to access the file.")

finally:
    print("End of script.")