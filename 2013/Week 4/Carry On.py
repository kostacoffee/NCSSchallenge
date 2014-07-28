def carries(a,b):
    carries = 0
    a = list(str(a))
    b= list(str(b))
    a.reverse()
    b.reverse()
    if (len(a) < len(b)):
        for i in range(len(a), len(b)):
            a.append("0")
    elif (len(b) < len(a)):
        for i in range(len(b), len(a)):
            b.append("0")
    a.append("0")
    b.append("0")
    r = range(len(a))
    for i in r:
        if (int(a[i]) + int(b[i]) >= 10):
            carries += 1
            if (i < r[-1]): a[i+1] = str(int(a[i+1])+1)
    return carries
