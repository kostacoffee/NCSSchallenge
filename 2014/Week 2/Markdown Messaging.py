import re

#captures reference declaration (keys with whitespace) r'\[(.*?)\]:(.*)'
#captures references r'\[.*?\](\[.*?\])'


def getReferences(lines):
    r = re.compile(r'\[(.*?)\]:(.*)')
    refs = {}
    for line in lines:
        match = r.search(line)
        if (match):
            refs[match.group(1)] = match.group(2).strip()
    return refs


def applyReferences(lines, references):
    r = re.compile(r'\[.*?\]\W*\[(.*?)\]')
    formattedLines = []
    for line in lines:
        while True:
            match = r.search(line)
            if(not match):
                break
            if (match.group(1) in references.keys()):
                line = line.replace('[' + match.group(1) + ']', '(' + references[match.group(1)] + ')')
        formattedLines.append(line)
    return formattedLines


def findMessage(lines):
    r = re.compile(r'\[.*?\]\W*\(.*?#(.*?)\)')
    words = []
    for line in lines:
        words.extend([x.strip() for x in r.findall(line) if x.strip() is not ''])
    return words

lines = open('post.md').readlines()
references = getReferences(lines)
lines = applyReferences(lines, references)
msg = findMessage(lines)
if (msg):
    print(" ".join(msg))
