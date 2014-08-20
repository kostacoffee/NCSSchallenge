def makeMapping(l):
    mapping = {}
    for i in range(len(l)):
        for c in l[i]:
            mapping[c] = str(i+2)
    return mapping

mapping = makeMapping('abc def ghi jkl mno pqrs tuv wxyz'.split())
freq = open('frequencies.txt').readlines()
freq = [(line.split()[0], int(line.split()[1])) for line in freq]
combFreq = {}
for wordFreq in freq:
    comb = "".join([mapping[c] for c in wordFreq[0]])
    if comb in combFreq.keys():
        combFreq[comb].append(wordFreq)
        combFreq[comb].sort(key=lambda x: x[1], reverse=True)
    else:
        combFreq[comb] = [wordFreq]
s = []
mapping = {str(i+2): 'adgjmptw'[i] for i in range(8)}
for comb in input().split():
    i = comb.count('*')
    comb = comb.replace('*', '')
    if (comb in combFreq.keys()):
        s.append(combFreq[comb][i%len(combFreq[comb])][0])
    else:
        ranS = ''
        for c in comb:
            ranS += mapping[c]
        s.append(ranS)
print(" ".join(s))
