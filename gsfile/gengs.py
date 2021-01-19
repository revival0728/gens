#this file is for generating source file

import os
import sys
import getopt

fn = ""
addr = ""

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:a:", ["filename=", "address="])
    for k, v in opts:
        if k == "-n":
            fn = v
        elif k == "-a":
            addr = v

except getopt.GetoptError:
    print("Something Went Wrong")
    quit()

if fn == "" or addr == "":
    print("Wrong Command")
    quit()

try:
    source = open(addr+"\\"+fn, "w")
    dfc = open("defaultcode.txt", "r")

    _fn = ""

    if fn.find(".") == -1:
        print("Missing file extension")
        quit()
    else:
        _fn = fn[:fn.find(".")]

    for i in dfc.readlines():
        s = i
        s = s.replace("\r", "")
        if not s.find("*FILENAME*") == -1:
            s = s.replace("*FILENAME*", _fn)
        source.write(s)

    source.close()

except:
    print("Address not found")
