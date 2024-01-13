#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, "r", encoding="UTF-8") as file:
        data = file.read()
        print(data, end="")
