import re
year = 0
month = 1
day = 2

f = open("ambiguous-dates.txt")
lines = f.readlines()
dates = []
dateFormat = [-1, -1, -1]
for line in lines:
    d = re.findall(r'([0-9]{1,4}\W[0-9]{1,4}\W[0-9]{1,4})', line)
    dates.extend(d)

intDates = []
for date in dates:
    dateElems = [int(x) for x in re.findall(r'([0-9]{1,4})', date)]
    intDates.append(dateElems)
    for i in range(3):
        if (dateElems[i] > 31):
            dateFormat[year] = i
        if (dateElems[i] > 12 and dateElems[i] < 32):
            dateFormat[day] = i

correctDates = []
if (dateFormat[year] == 0):
    dateFormat = [0, 1, 2]
elif (dateFormat[year] == 2):
    if (dateFormat[day] == 0):
        dateFormat = [2, 1, 0]
    elif (dateFormat[day] == 1):
        dateFormat = [2, 0, 1]
if dateFormat.count(-1) == 0:
    for date in intDates:
        correctFormat = [0, 0, 0]
        for i in range(3):
            correctFormat[i] = date[dateFormat[i]]
        correctDates.append(correctFormat)
    for date in correctDates:
        print("-".join(["%04d" % date[0], "%02d" % date[1], "%02d" % date[2]]))
else:
    print("No unambiguous dates found")
