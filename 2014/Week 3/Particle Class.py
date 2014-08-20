class Particle:

    def __init__(self, x, y, vx, vy, charge):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.charge = charge

    def disp(self):
        print('position = (%i, %i)' % (self.x, self.y))
        print('velocity = (%i, %i)' % (self.vx, self.vy))
        print('charge = ' + str(self.charge))

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def distance(self, x, y):
        return ((x-self.x)**2 + (y-self.y)**2)**(1/2)
