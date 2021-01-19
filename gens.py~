#this file is for user (loby)
#with command -w -p
#             -h
#             -scgs //save_changes
#             -upddc //update_default_code
#             -newdlt //add_new_download_tool
#             -newply //add_new_plugin
#             -settrf // set_target_file

import os
import sys
import getopt

erropt = "Unknown Command"
commands = "hw:p:scgs:upddc:newdlt:newply:settrf:"
command_list = ["help", "website=", "problemid=", "upd_default_code=", "new_download_tool=", "new_plugin=", "set_target_file="]
option = {
        "-w" : "",
        "-p" : "",
        "-upddc" : "",
        "-newdlt" : [],
        "-newply" : [],
        "-settrf" : ""
        }

try:
    opts, args = getopt.getopt(sys.argv[1:], commands, command_list)

    for k, v in opts:
        if k == "-h":
            guide = open(".\\guide\\guidebook.txt")
            for i in guide.readlines():
                print(i)
        elif not k in option:
            print(erropt)
            quit()
        elif not k.find(" ") == -1:
            option[k] = list(v.split())
        else:
            option[k] = v

except getopt.GetoptError:
    print(erropt)
    quit()
