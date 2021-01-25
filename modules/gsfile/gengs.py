#this file is for generating source file

import os
import sys
import getopt
from lib import compiler

def gengs(fn, addr):
    path = os.path.abspath(__package__)

    if fn == "" or addr == "":
        print("Wrong Command")
        quit()

    dfc = open(path+"\\"+"defaultcode.txt", "r")

   # try:

    ext = ""
    
    while ext == "":
        s = dfc.readline()
        ret = compiler.compiler(s)
        if not type(ret) == tuple:
            continue
        elif ret[1]:
            ext = ret[0]

    _fn = ""

    if fn.find(".") == -1:
        fn += ext

    if fn.find(".") == -1:
        print("Missing file extension")
        quit()
    else:
        _fn = fn[:fn.find(".")]
    
    source = open(addr+"\\"+fn, "w")

    print("generating {} source file ... ".format(fn))

    isnot_code = True

    for i in dfc.readlines():
        s = i.replace("\r", "")
        
        if s.strip() == "" and isnot_code:
            continue

        isnot_code = False

        s = compiler.compiler(s, filename = _fn)
        source.write(s)

    source.close()
   # except:
   #     print("Address not found")
   #     quit()

if __name__ == "__main__":
    try:
        fn = ""
        addr = ""
        opts, args = getopt.getopt(sys.argv[1:], "n:a:", ["filename=", "address="])
        for k, v in opts:
            if k == "-n":
                fn = v
            elif k == "-a":
                addr = v
        gengs(fn, addr)

    except getopt.GetoptError:
        print("Unknown Command")
        quit()
