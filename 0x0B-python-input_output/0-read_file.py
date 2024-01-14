#!/usr/bin/python3

# DEfine a function to read and print the contents of a text file
def read_file(filename=""):
    """ Reads the contents of a text file and prints it to the stdout

    Args:
    filename (str, access mode): The name of the file to read
    """
    # open the file in read mode with UTF-8 encoding
    with open(filename, "r", encoding="UTF-8") as file:
        #Reads the entire content of the file into a variable
        data = file.read()
        #print the file content to the stdout
        print(data, end="")
