def buildGames(draw):
    games = {}
    roundCopy = draw[:]
    nextRound= []
    for round in range(int(len(draw)**1/2)):
        for i in range(0, len(roundCopy), 2):
            if (len(roundCopy) < 2): return games
            matchCopy = roundCopy[:]
            t1 = matchCopy[i]
            t2 = matchCopy[i+1]
            games[(t1[0],t2[0])] = round+1
            if (t1[1] < t2[1]): nextRound.append(t1)
            else: nextRound.append(t2)
        roundCopy = nextRound[:]
        nextRound.clear()
    return games


def formatTeams(draw):
    teams = []
    for line in draw:
        t = line.strip().split(',')
        t[1] = int(t[1])
        teams.append(t)
    return teams

f = open('draw.txt')
draw = f.readlines()
games = buildGames(formatTeams(draw))
team = (input(), input())
if (team in games.keys()):
    print("Round " + str(games[team]))
elif (team[::-1] in games.keys()):
    print("Round " + str(games[team[::-1]]))
else:
    print("Did not play")
