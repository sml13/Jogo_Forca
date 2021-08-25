def countMax(upRight):
    a,b = [],[]
    for x in upRight:
        a.append(int(x.split(" ")[0]))
        b.append(int(x.split(" ")[1]))
    return min(a) * min(b)