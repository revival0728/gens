def compiler(s, filename = "", webname = "", functionname = "", url = ""):
    if not s.find("*FILENAME*") == -1:
        s = s.replace("*FILENAME*", filename)
    if not s.find("*FILEEXT*") == -1:
        s = s.split()[1]
        return s, 1
    if not s.find("*WEBNAME*") == -1:
        s = s.replace("*WEBNAME*", webname)
    if not s.find("*FUCNAME*") == -1:
        s = s.replace("*FUCNAME*", functionname)
    if not s.find("*URL*") == -1:
        s = s.replace("*URL*", url)
    return s
