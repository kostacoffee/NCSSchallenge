import csv
import math


def getDecimal(line):
    dms = [float(x) for x in line[:3]]
    deg = dms[0] + (dms[1]/60) + (dms[2]/3600)
    if (line[3] in 'SW'):
        deg = -deg
    return math.radians(deg)


def getAngle(lat1, long1, toilet):
    lat2 = math.radians(float(toilet['Latitude']))
    long2 = math.radians(float(toilet['Longitude']))
    return math.acos((math.sin(lat1)*math.sin(lat2)) + (math.cos(lat1)*math.cos(lat2)*math.cos(abs(long1-long2))))


allToilets = csv.DictReader(open('public-toilets.csv'))
allToilets = [t for t in allToilets if t['IsOpen'] != 'Variable']
latitude = getDecimal(input().split())
longitude = getDecimal(input().split())
hour = int(input())
if (hour < 6 or hour > 20):
    allToilets = [t for t in allToilets if t['IsOpen'] != 'DaylightHours']
lowest = allToilets[0]
lowest['Angle'] = getAngle(latitude, longitude, lowest)*6371
for toilet in allToilets[1:]:
    toilet['Angle'] = getAngle(latitude, longitude, toilet)*6371
    if (toilet['Angle'] < lowest['Angle']):
        lowest = toilet
print('Closest toilet: %s, %s, %s' % (lowest['Name'], lowest['Town'], lowest['State']))
print('Distance: ' + str(round(lowest['Angle'])) + 'km')
