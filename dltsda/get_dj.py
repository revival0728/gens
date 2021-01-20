import requests as rqs
from bs4 import BeautifulSoup as bsp

#f = open("out.txt", mode = "w")


def get_dj(url):

    res = rqs.get(url)

    html = bsp(res.text, "html.parser")
    data = html.findAll("div", {"class" : "problembox"})

    test_input = data[3].text
    test_output = data[4].text

    test_input = test_input.replace("\r", "")
    test_output = test_output.replace("\r", "")

    test_input = test_input[1:]
    test_output = test_output[1:]

    return test_input, test_output

if __name__ == "__main__":
    url = input()
    get_tsdata(url)


#f.close()
