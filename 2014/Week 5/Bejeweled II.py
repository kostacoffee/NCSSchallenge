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

    def __init__(self, jewels, extras):
        self.jewels = jewels
        self.score = 0
        self.extras = extras

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


    def swap(self, coords):
        for c in coords:
            if c not in range(8):
                print('Invalid move')
                return
        x1, y1, x2, y2 = coords
        if not((x1 == x2 + 1 or x1 == x2 - 1) and y1 == y2):
            if not((y1 == y2 + 1 or y1 == y2 - 1) and x1 == x2):
                print('Invalid move')
                return
        temp = self.jewels[7-y1][x1]
        self.jewels[7-y1][x1] = self.jewels[7-y2][x2]
        self.jewels[7-y2][x2] = temp
        cascadedRows = self.runRows(0)
        cascadedCols = self.runCols(0)
        if (not(cascadedRows or cascadedCols)):
            temp = self.jewels[y1][x1]
            self.jewels[7-y1][x1] = self.jewels[7-y2][x2]
            self.jewels[7-y2][x2] = temp
            print('Invalid move')
            return
        self.run()

    def substitute(self):
        for col in range(8):
            for row in range(7,-1,-1):
                if (type(jewels[row][col]) == QJewel):
                    jewels[row][col] = Jewel(self.extras[0])
                    self.extras = self.extras[1:]

    def run(self):
        multiplier = 1
        while True:
            cascadedRows = self.runRows(multiplier)
            cascadedCols = self.runCols(multiplier)
            if (not(cascadedRows or cascadedCols)):
                break
            self.cascade()
            multiplier += 1
            self.substitute()
        self.printResult()

    def runRows(self, multiplier):
        cascaded = False
        for row in range(6):
            for col in range(8):
                match = self.jewels[row:row+3]
                if (match[0][col].label == match[1][col].label == match[2][col].label):
                    cascaded = self.jewels[row][col].setCascaded()
                    self.jewels[row+1][col].setCascaded()
                    self.jewels[row+2][col].setCascaded()
                    if cascaded:
                        self.score += 10*multiplier
        return cascaded

    def runCols(self, multiplier):
        cascaded = False
        for row in range(8):
            for col in range(6):
                match = self.jewels[row][col:col+3]
                if (match[0].label == match[1].label == match[2].label):
                    cascaded = self.jewels[row][col].setCascaded()
                    self.jewels[row][col+1].setCascaded()
                    self.jewels[row][col+2].setCascaded()
                    if cascaded:
                        self.score += 10*multiplier
        return cascaded

line = open('jewels.txt').readline().strip()
lines = [line[i:i+8] for i in range(0, 64, 8)][::-1]
extras = line[64:]
jewels = [[Jewel(c) for c in line] for line in lines]
print('\n'.join([' '.join(line) for line in lines]))
print('Score = 0')
board = Board(jewels, extras)
while True:
    inp = input()
    if (inp == ''):
        break
    board.swap([int(x) for x in inp.split()])
