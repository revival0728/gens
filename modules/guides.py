#this file is for command -h or --help

from guide import open_guides
from guide import read_guides

def guides():
    print("Here are guide books\nPick the one which can help you!")
    read_guides.read_guides()
    num = input()
    if not num.isdecimal():
        print("Option Error")
        quit()
    else:
        if not open_guides.open_guides(int(num)):
            print("Option Error")
            quit()

if __name__ == "__main__":
    guides()
