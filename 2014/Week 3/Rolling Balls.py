holes = [[int(line.split()[0]), int(line.split()[1])] for line in open('holes.txt').readlines()]
balls = [(int(line.split()[0]), line.split()[1]) for line in open('balls.txt').readlines()]
bucket = []
for ball in balls:
    inBucket = True
    for hole in holes:
        if (hole[0] >= ball[0]  and hole[1] > 0):
            hole[1] -= 1
            inBucket = False
            break
    if (inBucket):
        bucket.append(ball)

if (len(bucket) > 0):
    print("The bucket contains: " + ', '.join([ball[1] for ball in bucket]) + '.')
else:
    print('The bucket contains no balls.')
