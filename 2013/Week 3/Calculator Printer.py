class CalcNum():

    def __init__(self, width, num, last):
        self.width = width
        self.num = num
        self.calcRep = []
        self.last = last
        self.generateCalcArray()
        self.actions = [self.make0, self.make1, self.make2, self.make3, self.make4, self.make5, self.make6, self.make7, self.make8, self.make9]
        self.actions[num]()
        if (not self.last): self.add(" ")

    def add(self, c):
        for i in range(len(self.calcRep)):
            if (i != len(self.calcRep)): self.calcRep[i].append(c)

    def make0(self):
        self.top()
        self.bot()
        self.topRight()
        self.bottomRight()
        self.topLeft()
        self.bottomLeft()

    def make1(self):
        self.topRight()
        self.bottomRight()

    def make2(self):
        self.top()
        self.mid()
        self.bot()
        self.topRight()
        self.bottomLeft()

    def make3(self):
        self.top()
        self.mid()
        self.bot()
        self.bottomRight()
        self.topRight()

    def make4(self):
        self.mid()
        self.topLeft()
        self.topRight()
        self.bottomRight()

    def make5(self):
        self.top()
        self.mid()
        self.bot()
        self.topLeft()
        self.bottomRight()

    def make6(self):
        self.top()
        self.mid()
        self.bot()
        self.topLeft()
        self.bottomRight()
        self.bottomLeft()

    def make7(self):
        self.top()
        self.topRight()
        self.bottomRight()

    def make8(self):
        self.top()
        self.mid()
        self.bot()
        self.topLeft()
        self.topRight()
        self.bottomLeft()
        self.bottomRight()

    def make9(self):
        self.top()
        self.mid()
        self.bot()
        self.topLeft()
        self.topRight()
        self.bottomRight()

    def getCalcRep(self):
        return self.calcRep

    def generateCalcArray(self):
        for col in range(2*self.width + 3):
            r= []
            for row in range(self.width + 2):
                r.append(" ")
            self.calcRep.append(r)

    def topRight(self):
        for i in range(1,self.width+1):
            self.calcRep[i][-1] = "|"

    def bottomRight(self):
        for i in range(-2,-self.width-2,-1):
            self.calcRep[i][-1] = "|"

    def topLeft(self):
        for i in range(1,self.width+1):
            self.calcRep[i][0] = "|"

    def bottomLeft(self):
        for i in range(-2,-self.width-2,-1):
            self.calcRep[i][0] = "|"

    def top(self):
        for i in range(1,self.width+1):
            self.calcRep[0][i] = "-"

    def mid(self):
        for i in range(1,self.width+1):
            self.calcRep[self.width+1][i] = "-"

    def bot(self):
        for i in range(1,self.width+1):
            self.calcRep[-1][i] = "-"


def main():
    num = input("Number: ")
    width = input("Width: ")
    calcNums = []
    out = ["" for i in range(2*int(width) + 3)]
    for i in range(len(num)):
        calcNums.append(CalcNum(int(width),int(num[i]), (i==len(num)-1)).getCalcRep())
    for line in range(2*int(width) + 3):
        for j in range(len(calcNums)):
            out[line] += "".join(calcNums[j][line])
    for line in out:
        print(line)
main()
