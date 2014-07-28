# Enter your code for "Chuck A Word 180" here.
lines = []
reversedLines = []
while True:
    line = input("Line: ")
    if (len(line) == 0): break
    lines.append(line)

for i in range(0, len(lines)):
    words = lines[i].split()
    newWords = []
    for j in range(0, len(words)):
        reversed = words[j][::-1]
        newWords.append(reversed)
    reversedLines.append(newWords)
for i in range(0, len(reversedLines)):
    print(" ".join(reversedLines[i]))
