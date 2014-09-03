def convert_grokcoin(x, knownCoins={}):
    x1 = int(x/2)
    x2 = int(x/3)
    x3 = int(x/4)
    if (x1 + x2 + x3 > x):
        for key in [x1, x2, x3]:
            if (key not in knownCoins.keys()):
                knownCoins[key] = int(convert_grokcoin(key, knownCoins))
        return knownCoins[x1] + knownCoins[x2] + knownCoins[x3]
    else:
        return x
