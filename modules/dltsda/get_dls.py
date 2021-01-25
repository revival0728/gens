#this file will return dlweblist.txt in format [{dict},{dict}, ...] // "webname", "url", "filename"

import os
import sys

def get_dls():
    path = os.path.abspath(__package__)
    weblist = open(path+"\\"+"dlweblist.txt", "r")
    ret = []
    for s in weblist.readlines():
        d = {}
        tmp = s.split()
        
        d.update({"webname" : tmp[0]})
        d.update({"url" : tmp[1]})
        d.update({"filename" : tmp[2]})
        ret.append(d)
        
    weblist.close()
    
    return ret
