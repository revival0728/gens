#this file is for user (loby)
#commands     -w | --web <website> -p | --pid <problemid> // gen and dl file
#             -h | --help // output guidebook.txt
#             -s | --scgs // save changes
#             -u | --upddc <file> // update default code
#             -d | --newdlt "<file> <file address>" // add new download tool
#             -g | --newply "<command file> <plugin file>" // add new plugin
#             -f | --settrf <folder> // set target folder

import os
import sys
import getopt

erropt = "Unknown Command"
commands = "hsw:p:u:d:g:f:"
command_list = ["help", "scgs", "web=", "pid=", "upddc=", "newdlt=", "newply=", "settrf="]

try:
    opts, args = getopt.getopt(sys.argv[1:], commands, command_list)

    web = ""
    pid = ""

    for k, v in opts:
        if k in ("-h", "--help"):
            guide = open("guide\\guidebook.txt")
            for i in guide.readlines():
                print(i.replace("\r", ""))
        elif k in ("-s", "--scgs"):
            pass
        elif k in ("-w", "--web"):
            web = v
        elif k in ("-p", "--pid"):
            pid = v
        elif k in ("-u", "--upddc"):
            pass
        elif k in ("-d", "--newdlt"):
            pass
        elif k in ("-g", "--newply"):
            pass
        elif k in ("-f", "--settrf"):
            pass

except getopt.GetoptError:
    print(erropt)
    quit()
