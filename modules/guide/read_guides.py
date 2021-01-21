#this file is for open guidelist.txt

import os

def read_guides(is_ret = 0):
    path = os.path.abspath(__file__)[:-14] + "\\"
    guidelist = open(path+"guidelist.txt", "r")
    num = 1
    ret = []
    for f in guidelist.readlines():
        if is_ret:
            ret.append(f.strip())
        else:
            print("({}) {}".format(num, f.strip()[:-4]))
            num += 1
    if is_ret:
        return ret

if __name__ == "__main__":
    read_guides()
