#this file is for print books

import os
from . import read_guides

def open_guides(num):
    path = os.path.abspath(__file__)[:-14] + "\\"
    gdlist = read_guides.read_guides(1)
    num -= 1
    if num >= len(gdlist) or num < 0:
        return False
    else:
        tarf = open(path+"books\\"+gdlist[num], "r")
        for w in tarf.readlines():
           print(w.replace("\r", ""))
        return True

if __name__ == "__main__":
    read_guides.read_guides()
    num = int(input())
    is_input_right = open_guides(num)
