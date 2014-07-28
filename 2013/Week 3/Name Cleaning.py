import re

alphabet = "abcdefghijklmnopqrstuvwxyz"

def main():
    LB = [line.strip() for line in open("leaderboard.txt",'r').readlines()]
    entries = []
    for line in LB:
        line = line.split(',')
        name = line[0]
        score = int(line[1])
        name = re.sub(r'^[0-9].*?([A-Z])', r'\1', name)
        name = name.split()
        name[0] = re.sub(r'^[A-Z][^a-z]*?([A-Z][a-z])',r'\1',name[0])
        name = " ".join(name)
        name = name.split()
        replaceName = name.copy()
        for word in replaceName:
            if (word.isupper()): name.remove(word)
            elif not word[0].isupper():
                name.remove(word)
        name = " ".join(name)
        name.strip()
        if(re.match(r'^[^A-Za-z_]*$', name)):
           name = "Invalid Name"
        entries.append((name, -abs(score)))
    entries = sorted(entries, key = lambda x: (x[1], x[0]))
    for entry in entries:
        print("%s,%i" % (entry[0], -entry[1]))





main()
