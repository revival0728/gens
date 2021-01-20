#this file is the main code of this project

from gsfile import lib
from gsfile import gengs
from dltsda import get_dls

def engin(web, pid):
    if web == "" or pid == "":
        print("Wrong Command use -h or --help to look up the guidebook")
        quit()

    weblist = get_dls.get_dls()
    print(weblist)

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
