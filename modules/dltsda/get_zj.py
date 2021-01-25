import requests as rqs
from bs4 import BeautifulSoup as bsp
def get_zj(url):

    res = rqs.get(url)
    ques=[] #test input
    str_ques=""
    ans=[] #test output
    str_ans=""
    tmp=[]
    html = bsp(res.text, "html.parser")
    data = html.findAll("div", {"class" : "problembox"})
    data2 = html.findAll("pre")

    for i in data2:
        if i.text!="\r" and i.text!="\r\n":
            tmp.append(i.text+"\n")

    for i in range(0,len(tmp),2):
        ques.append(tmp[i])
        ans.append(tmp[i+1])

    for i in ques:
            str_ques+=i
    for i in ans:
            str_ans+=i
            
    str_ques=str_ques.replace("\n\n","\n")
    str_ans=str_ans.replace("\n\n","\n")

    str_ques=str_ques.replace("\r","")
    str_ans=str_ans.replace("\r","")

    return str_ques,str_ans
if __name__ == "__main__":
    url = input()
    get_zj(url)
