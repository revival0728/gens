#this file is for updating defaultcode.txt

import os
import sys
import getopt

def upddc(addr):
    path = os.path.abspath(__file__)
    path = path[:-8]

    if addr == "":
        print("Address is empty")

    try:
        ndc = open(addr, "r")
        dc = open(path+"\\"+"defaultcode.txt", "w")
        for i in ndc.readlines():
            dc.write(i.replace("\r", ""))
        dc.close()

    except:
        print("File not found")

if __name__ == "__main__":

    addr = ""
    try:
        opts, args = getopt.getopt(sys.argv[1:], "a:", ["address="])
        for k, v in opts:
            if k == "-a":
                addr = v.replace("\\", "\\\\")
        upddc(addr)

    except getopt.GetoptError:
        print("Something Wrong")
        quit()
