#!/usr/bin/python3
# ! -- means shebang, an instruction to the python interpreter


def file_function():
    # Open a file
    fo = open("foo12.txt", "r")
    print("Name of the file: ", fo.name)
    for line in fo:
        print(line.strip())
    # Close opened file
    fo.close()

# main code
file_function()
