consonants = 'bcdfghjklmnpqrstvwxyz'
upperConsonants = consonants.upper()


def encode(s):
    finalStr = ''
    if (s.istitle() and s[0] in upperConsonants):
        finalStr = s[0] + 'o' + s[0].lower()
        s = s[1:]
    for c in s:
        if (c in consonants):
            finalStr += c + 'o' + c
        elif c in upperConsonants:
            finalStr += c + 'O' + c
        else:
            finalStr += c
    return finalStr


def decode(s):
    finalStr = ''
    i = 0
    if s.istitle() and s[0] in upperConsonants:
        finalStr += s[0]
        s = s[3:]
    while i < len(s):
        tempS = s[i:i+3].lower()
        if not len(tempS) == 3:
            finalStr += tempS
            break
        finalStr += s[i]
        if (tempS[0] in consonants and tempS == (tempS[0] + 'o' + tempS[2])):
            i += 3
        else:
            i += 1
    return finalStr

    print(decode('totootot'))
