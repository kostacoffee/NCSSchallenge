def vicinicals(words):
    vic = []
    nonVic = []
    for word in words:
        charsWithNeighbours = 0
        for c in word:
            neighbours = [ord(c) + 1, ord(c) - 1]
            otherCase = -32
            if c.isupper():
                otherCase = 32
            neighbours.extend([ord(c) + otherCase + 1, ord(c) + otherCase - 1])
            if (c == "A" or c == "a"):
                neighbours.remove(64)
                neighbours.remove(96)
                neighbours.extend([ord('z'), ord('Z')])
            if (c == "Z" or c == "z"):
                neighbours.remove(91)
                neighbours.remove(123)
                neighbours.extend([ord('a'), ord('A')])
            for n in neighbours:
                if (chr(n) in word and ((n >= 65 and n <= 90) or (n >= 97 and n <= 122))):
                    charsWithNeighbours += 1
                    break
        if len(word) == charsWithNeighbours:
            vic.append(word)
        elif charsWithNeighbours == 0:
            nonVic.append(word)
    if (len(vic) > 0):
        print("Vicinals: " + " ".join(vic))
    if (len(nonVic) > 0):
        print("Non-vicinals: " + " ".join(nonVic))

while True:
    line = input()
    if line == "":
        break
    vicinicals(line.split())
