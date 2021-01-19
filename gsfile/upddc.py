#this file is for updating defaultcode.txt

import os
import sys
import getopt

addr = ""

try:
    opts, args = getopt.getopt(sys.argv[1:], "a:", ["address="])
    for k, v in opts:
        if k == "-a":
            addr = v.replace("\\", "\\\\")

except getopt.GetoptError:
    print("Something Wrong")
    quit()

if addr == "":
    print("Address is empty")

try:
    ndc = open(addr, "r")
    dc = open("defaultcode.txt", "w")
    for i in ndc.readlines():
        dc.write(i.replace("\r", ""))

except:
    print("File not found")
