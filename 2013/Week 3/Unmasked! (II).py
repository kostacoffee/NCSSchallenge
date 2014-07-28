import string

class Writing:
    def __init__(self, filename):
        self.filename = filename.strip()
        self.words = open(self.filename,'r').read().split()
        self.words = self.removePunc(self.words)
        self.unkWords = open("unknown.txt",'r').read().split()
        self.unkWords = self.removePunc(self.unkWords)
        self.lengths = self.getLengths(self.words)
        self.unkLengths = self.getLengths(self.unkWords)
        if (len(self.lengths) < len(self.unkLengths)):
            currentLen = len(self.lengths)
            for i in range(currentLen,len(self.unkLengths)):
                self.lengths.append(0)
        elif (len(self.lengths) > len(self.unkLengths)):
            currentLen = len(self.unkLengths)
            for i in range(currentLen, len(self.lengths)):
                self.unkLengths.append(0)
        self.sim = self.calcSim()

    def getResult(self):
        return (self.sim, self.filename)

    def calcSim(self):
        multSum = 0
        root1Sum = 0
        rootUnkSum = 0
        for i in range(len(self.lengths)):
            multSum += self.lengths[i] * self.unkLengths[i]
            root1Sum += self.lengths[i]**2
            rootUnkSum += self.unkLengths[i]**2
        root1Sum = root1Sum**0.5
        rootUnkSum = rootUnkSum**0.5
        return multSum/(rootUnkSum * root1Sum)

    def removePunc(self, words):
        for i in range(len(words)):
            words[i] = words[i].strip(string.punctuation)
        return words

    def getLengths(self, words):
        lengths = []
        for word in words:
            currentLen = len(lengths)
            if (len(word) == 0): continue
            if (len(word) >= currentLen):
                for i in range(currentLen, len(word)):
                    lengths.append(0)
            lengths[len(word)-1] += 1
        return lengths



def main():
    results = []
    for text in open("texts.txt",'r').readlines():
        results.append(Writing(text).getResult())
    results.sort(key=lambda x:x[0], reverse = True)
    for sim,text in results:
        print("%.3f %s" % (sim,text))


main()
