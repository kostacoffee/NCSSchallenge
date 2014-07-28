scores = {}
versusArray = []
with open("commentary.txt", 'r') as commentary:
    versusLine = commentary.read()
    versusLine = versusLine.replace("versus", "")
    versusArray = versusLine.split()
    scores[versusArray[0]] = 0
    scores[versusArray[1]] = 0
f = open("commentary.txt", 'r')
skipped = False
for line in f.readlines():
    if (not skipped):
        skipped = True
        continue
    line = line.split()
    scores[line[0]] +=1
f.close()
if (scores[versusArray[0]] > scores[versusArray[1]]):
    print(versusArray[0] + " " + str(scores[versusArray[0]]) + "\n" + versusArray[1] + " " + str(scores[versusArray[1]]))
else: print(versusArray[1] + " " + str(scores[versusArray[1]]) + "\n" + versusArray[0] + " " + str(scores[versusArray[0]]))
