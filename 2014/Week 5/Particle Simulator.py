class Particle:

    def __init__(self, stats):
        self.x = stats[0]
        self.y = stats[1]
        self.vx = stats[2]
        self.vy = stats[3]
        self.charge = int(stats[4])
        self.ax = stats[5]
        self.ay = stats[6]

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if (self.x >= 300 or self.x <= -300):
            self.vx = -self.vx
            if (self.x > 300):
                self.x = 300.0
            elif self.x < -300:
                self.x = -300.0
        if (self.y >= 200 or self.y <= -200):
            self.vy = -self.vy
            if self.y > 200:
                self.y = 200.0
            elif self.y < -200:
                self.y = -200.0

    def accelerate(self):
        self.vx += self.ax
        self.vy += self.ay

    def getPos(self):
        return str(round(self.x, 1))+','+str(round(self.y, 1))


def calcAccel(particles):
    for part in particles:
        sameCharge = set([p for p in particles if p.charge == part.charge])
        oppCharge = set([p for p in particles if p.charge == -part.charge])
        high = set([p for p in particles if p.y > part.y])
        low = set([p for p in particles if p.y < part.y])
        left = set([p for p in particles if p.x < part.x])
        right = set([p for p in particles if p.x > part.x])
        part.vx += (len(sameCharge & left) + len(oppCharge & right) - len(sameCharge & right) - len(oppCharge & left))/10.0
        part.vy += (len(sameCharge & low) + len(oppCharge & high) - len(sameCharge & high) - len(oppCharge & low))/10.0

particles = []
lines = [line.strip().split() for line in open('particles.txt').readlines()]
its = int(lines[0][0])
for line in lines[1:]:
    particles.append(Particle([float(s) for s in line]))
for i in range(its, 0, -1):
    calcAccel(particles)
    [p.move() for p in particles]
    print(','.join([p.getPos() for p in particles]))
