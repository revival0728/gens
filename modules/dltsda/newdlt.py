import os
import shutil
def newdlt(txt_addr,code_name,code_addr):
    path=os.path.abspath(__file__)
    path=path[:-10]

    file0=open(txt_addr,"r")
    dlweblist=open(path+"\\"+"dlweblist.txt","a")

    txt_str=file0.read()
    dlweblist.write("\n"+txt_str)

    shutil.copyfile(code_addr+"\\"+code_name,code_addr+"\\df7^$%^hjkxGK&.py")
    shutil.move(code_addr+"\\"+code_name,path)
    os.rename(code_addr+"\\"+"df7^$%^hjkxGK&.py",code_addr+"\\"+code_name)

    file0.close()
    dlweblist.close()

if __name__=="__main__":
    newdlt(r"C:\Users\Administrator\Desktop\123.txt","tet.py",r"C:\Users\Administrator\Desktop")
