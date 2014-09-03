def countSkin(room, Srow, Scol):
    skins = 0
    todo = [(Srow, Scol)]
    while len(todo) > 0:
        row, col = todo[0]
        todo = todo[1:]
        if (row in range(len(room)) and col in range(len(room[row]))):
            if (room[row][col] == 'X'):
                skins += 1
                room[row][col] = '.'
                todo.append((row, col + 1))
                todo.append((row, col - 1))
                todo.append((row + 1, col))
                todo.append((row - 1, col))
                todo = list(set(todo))
    return skins


def findHead(room):
    global skins
    for row in range(len(room)):
        for col in range(len(room[row])):
            if room[row][col] == '<':
                skins = 1
                return (row, col + 1)
            elif room[row][col] == '>':
                skins = 1
                return (row, col - 1)
            elif room[row][col] == 'v':
                skins = 1
                return (row - 1, col)
            elif room[row][col] == '^':
                skins = 1
                return (row + 1, col)


room = [list(line.strip()) for line in open('room.txt').readlines()]
skins = 0
coords = findHead(room)
if skins == 1:
    skins += countSkin(room, coords[0], coords[1])
print(skins)
