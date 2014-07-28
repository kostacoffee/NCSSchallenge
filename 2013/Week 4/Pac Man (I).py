class Ghost:

    def __init__(self, posY, posX, pacY, pacX, maze):
        self.posY = posY
        self.posX = posX
        self.pacX = pacX
        self.pacY = pacY
        self.maze = maze
        self.newPlace = self.moveGhost()

    def moveGhost(self):
        todo = [[(self.posY, self.posX)]]
        while (len(todo) > 0):
            path = todo.pop(0)
            if (path[-1] == (self.pacY,self.pacX)):
                self.maze[self.posY][self.posX] = " "
                return path[1]
            latestPath = path[-1]
            pathSet = [(latestPath[0]-1,latestPath[1]),(latestPath[0],latestPath[1]-1),(latestPath[0]+1,latestPath[1]),(latestPath[0], latestPath[1]+1)]
            for possiblePath in pathSet:
                if (self.maze[possiblePath[0]][possiblePath[1]] != "#" and possiblePath not in path):
                    p = path.copy()
                    p.append(possiblePath)
                    todo.append(p)



def main():
    mazeLines = open("maze.txt", 'r').readlines()
    maze = []
    for line in mazeLines:
        maze.append(list(line.strip()))
    for col in range(0, len(maze)):
        for row in range(0, len(maze[col])):
            if (maze[col][row] == "P"):
                pacY = col
                pacX = row
    newGhosts = []
    for col in range(0, len(maze)):
        for row in range(0, len(maze[col])):
            if (maze[col][row] == "G"):
                newGhosts.append(Ghost(col, row, pacY, pacX, maze).newPlace)
    for col in range(0, len(maze)):
        for row in range(0, len(maze[col])):
            if ((col,row) in newGhosts):
                maze[col][row] = "G"
    for line in maze:
        line = "".join(line)
        print(line)

main()
