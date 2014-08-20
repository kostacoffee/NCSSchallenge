#<(\w+)(?: .*?)? */> DOTALL self-closing
#<(\w+)(?: .*?)?\s*> DOTALL open

#<(\w+)(?: .*?)?(?: */|\s*)> factorised the above
import re

s = open('input.html').read()
f = re.findall(r'<(\w+)(?: .*?)?(?: */|\s*)>', s, re.DOTALL)
freq = {}
for tag in f:
    tag = tag.lower()
    if tag in freq.keys():
        freq[tag] += 1
    else:
        freq[tag] = 1

tagFreq = sorted(freq, key=lambda x: len(x), reverse=True)
tagFreq.sort(key=freq.get, reverse=True)
for i in range(len(tagFreq)):
    if (len(tagFreq[i]) == len(tagFreq[0]) and freq[tagFreq[i]] == freq[tagFreq[0]]):
        print(tagFreq[i], freq[tagFreq[i]])
