class Line:

    def __init__(self, x1, y1, x2, y2, label):
        if x1 > x2:
            self.endX = x1
            self.endY = y1
            self.startX = x2
            self.startY = y2
        else:
            self.endX = x2
            self.endY = y2
            self.startX = x1
            self.startY = y1
        self.grad = (y1 - y2)/(x1 - x2)
        self.yInt = y1 - self.grad*x1
        self.label = label

    def __str__(self):
        return self.label

    def getY(self, x):
        return x*self.grad + self.yInt


class Ball:

    def __init__(self, x, y, lines):
        self.x = x
        self.y = y
        self.lines = lines
        self.linesFallen = []
        self.startFall()

    def startFall(self):
        while self.y >= 0:
            self.fall()
            if (self.hitGround()):
                break

    def hitGround(self):
        if (self.y <= 0):
            self.y = -1
            self.linesFallen.append('GROUND')
            print(' '.join(self.linesFallen))
            return True
        return False

    def fall(self):
        linesBelow = []
        for line in self.lines:
            if (self.x >= line.startX and self.x <= line.endX):
                linesBelow.append(line)
        self.linesBelow = [line for line in linesBelow if self.y >= line.getY(self.x)]
        self.linesBelow.sort(key=lambda x: x.getY(self.x), reverse=True)
        if len(self.linesBelow) > 0:
            self.roll(self.linesBelow[0])
        else:
            self.y = -1


    def roll(self, line):
        self.linesFallen.append(str(line))
        if (line.grad < 0):
            self.x = line.endX
            self.y = line.endY
        else:
            self.x = line.startX
            self.y = line.startY
        self.lines.remove(line)

props = open('marble-run.txt').readlines()
ballProps = [float(x) for x in props[0].strip().split()]
lines = []
for i in range(1, len(props)):
    lineProps = props[i].split()
    label = lineProps[0]
    lineProps = [float(x) for x in lineProps[1:]]
    lines.append(Line(lineProps[0], lineProps[1], lineProps[2], lineProps[3], label))
Ball(ballProps[0], ballProps[1], lines).startFall()
