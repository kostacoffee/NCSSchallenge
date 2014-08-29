import re

words = []
while True:
    line = input().strip()
    if (line == ''):
        break
    words.extend([x.lower() for x in re.split(r'[ |,|;|.|-]', line) if len(x) >= 4])
typos = {}
for word in words:
    noVowel = word[:]
    for c in word:
        if (c in 'aeiou'):
            noVowel = noVowel.replace(c, '')
    if (noVowel in typos.keys()):
        typos[noVowel].append(word)
        typos[noVowel] = list(set(typos[noVowel]))
    else:
        typos[noVowel] = [word]
for key in typos:
    if (len(typos[key]) > 1):
        print(' '.join(sorted(typos[key])))
