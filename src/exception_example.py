#!/usr/bin/python3

fh = None
try:
    fh = open("testfile", "r")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")
finally:
    print("Written content in the file successfully")
    if fh:
        fh.close()
