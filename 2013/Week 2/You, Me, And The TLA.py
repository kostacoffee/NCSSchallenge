import re

def main():
    with open("sentences.txt", 'r') as f: lines = f.readlines()
    TLAlines = 0
    for line in lines:
        line = re.findall(r"[^.,!?;_\W]+", line)
        for word in line:
            reg = re.compile(r'^[^A-Z]*([A-Z]{3})[^A-Z]*$')
            if (reg.match(word)):
                TLAlines += 1
                break
    perc = "%0.1f" % (float(TLAlines)/len(lines) * 100)
    print(perc + "% of sentences contain a TLA")

main()
