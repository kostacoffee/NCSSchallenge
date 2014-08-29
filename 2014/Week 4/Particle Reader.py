from particle import Particle

def checkLineErrors(line, n):
    if len(line) > 5:
        raise RuntimeError('Line %i contains too many items' % n)
    elif (len(line) < 5):
        raise RuntimeError('Line %i contains too few items' % n)
    for val in line:
        try:
            float(val)
        except ValueError:
            raise TypeError('Line %i has a non-number' % n)
    if (float(line[4]) not in [-1, 0, 1]):
        raise ValueError('Line %i has an invalid charge' % n)

def load_particles(filename):
    # returns a list of Particles created
    # from filename, or raises an Exception
    lines = [line.strip().split() for line in open(filename).readlines()]
    particles = []
    for i in range(len(lines)):
        line = lines[i]
        if len(line) == 0:
            continue
        checkLineErrors(line, i+1)
        p = Particle(float(line[0]), float(line[1]), float(line[2]), float(line[3]), float(line[4]))
        for part in particles:
            if (p.x == part.x and p.y == part.y):
                raise ValueError('Line %i uses the same position as a previous particle' % (i+1))
        particles.append(p)
    return particles

try:
    l = load_particles("particles.txt")
except RuntimeError as e:
    # we check that the following is printed
    # with the correct message for this file
    print("Raised RuntimeError", e)
except TypeError as e:
    # other Exceptions left as an exercise for you!
    print("Raised TypeError", e)
except ValueError as e:
    print('Raised ValueError', e)
