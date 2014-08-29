class Jewel:

    def __init__(self, label):
        self.label = label
        self.cascaded = False

    def setCascaded(self):
        self.cascaded = True
        return True

    def __str__(self):
        return self.label

class QJewel(Jewel):

    def __init__(self):
        self.label = '?'
        self.cascaded = False

    def setCascaded(self):
        return False

class Board:

    def __init__(self, jewels):
        self.jewels = jewels
        self.score = 0

    def fall(self, row, col):
        for i in range(row, 0, -1):
            temp = self.jewels[i][col]
            self.jewels[i][col] = self.jewels[i-1][col]
            self.jewels[i-1][col] = temp
        for i in range(8):
            if (self.jewels[0][i].cascaded):
                self.jewels[0][i] = QJewel()


    def cascade(self):
        for row in range(8):
            for col in range(8):
                if self.jewels[row][col].cascaded:
                    self.fall(row, col)

    def printResult(self):
        lines = []
        for line in self.jewels:
            strLine = []
            for j in line:
                strLine.append(str(j))
            lines.append(' '.join(strLine))
        print('\n'.join(lines))
        print('Score = %i' %(self.score))


    def run(self):
        while True:
            cascadedRows = self.runRows()
            cascadedCols = self.runCols()
            if (not(cascadedRows or cascadedCols)):
                break
            self.cascade()
        self.printResult()

    def runRows(self):
        cascaded = False
        for row in range(6):
            for col in range(8):
                match = self.jewels[row:row+3]
                if (match[0][col].label == match[1][col].label == match[2][col].label):
                    cascaded = self.jewels[row][col].setCascaded()
                    self.jewels[row+1][col].setCascaded()
                    self.jewels[row+2][col].setCascaded()
                    if cascaded:
                        self.score += 10
        return cascaded

    def runCols(self):
        cascaded = False
        for row in range(8):
            for col in range(6):
                match = self.jewels[row][col:col+3]
                if (match[0].label == match[1].label == match[2].label):
                    cascaded = self.jewels[row][col].setCascaded()
                    self.jewels[row][col+1].setCascaded()
                    self.jewels[row][col+2].setCascaded()
                    if cascaded:
                        self.score += 10
        return cascaded

line = open('jewels.txt').readline().strip()
lines = [line[i:i+8] for i in range(0, len(line), 8)][::-1]
jewels = [[Jewel(c) for c in line] for line in lines]
print('\n'.join([' '.join(line) for line in lines]))
print('Score = 0')
Board(jewels).run()
