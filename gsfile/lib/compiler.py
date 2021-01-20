def compiler(s, fn = ""):
    if not s.find("*FILENAME*") == -1:
        s = s.replace("*FILENAME*", fn)
    if not s.find("*FILEEXT*") == -1:
        s = s.split()[1]
        return s, 1
    return s
