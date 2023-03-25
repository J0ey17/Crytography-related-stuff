teststr = "RTGHGT KTQP HQQF CITGG"
s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


for i in range(1, 27):
    res = ""
    for j in teststr:
        if j == ' ':
            res += ' '
            continue
        res += s[s.find(j)-i]
    print(res)
