#this file will return dlweblist.txt in format [{dict},{dict}, ...] // "webname", "url", "filename"

import os
import sys

def get_dls():
    path = os.path.abspath(__package__)
    weblist = open(path+"\\"+"dlweblist.txt", "r")
    ret = []
    for s in weblist.readlines():
        tmp = s.split()
        ret.append({("webname", tmp[0]), ("url", tmp[1]), ("filename", tmp[2])})
    weblist.close()
    
    return ret
