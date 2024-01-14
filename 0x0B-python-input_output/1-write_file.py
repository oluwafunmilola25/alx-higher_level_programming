#!/usr/bin/python3

def write_file(filename="", text=""):
    with open(fiename, "w", encoding="UTF-8") as file:
        data = file.write(text)
        return data
