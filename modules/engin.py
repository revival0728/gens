#this file is the main code of this project

import os
from gsfile import gengs
from dltsda import get_dls
from lib import compiler

def engin(web, pid):
    path = os.path.abspath(__file__)
    path = path[:-8]

    if web == "" or pid == "":
        print("Wrong Command use -h or --help to look up the guidebook")
        quit()

    gengs.gengs(pid, ".")
    weblist = get_dls.get_dls()

    fcode = open(path+"\\"+"enginC\\code.txt")
    code = ""
    for i in fcode.readlines():
        code += i.replace("\r", "")
    print(compiler.compiler(code, webname = web, functionname = weblist[0]["filename"][:-3]))
    #pid[:-3] -> test.py -> test

if __name__ == "__main__":
    import getopt
    import sys
    import os

    try:
        opts, args = getopt.getopt(sys.argv[1:], "w:p:", ["web=", "pid="])

        web = ""
        pid = ""

        for k, v in opts:
            if k in ("-w", "--web"):
                web = v
            elif k in ("-p", "--pid"):
                pid = v

        if web == "" or pid == "":
            print("Wrong Command")
            quit()

        engin(web, pid)

    except getopt.GetoptError:
        print("Unknown Command")
        quit()
