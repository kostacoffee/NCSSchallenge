import csv
import sys

def getDegree(code, degrees):
    for degree in degrees:
        if (degree["code"] == code): return degree

def getEnrolledStudents(degreeCode):
    allEnrolls = []
    for student in students:
        if (degreeCode == student['offer']):
            allEnrolls.append(student)
    allEnrolls.sort(key = lambda x: x['name'], reverse = True)
    allEnrolls.sort(key = lambda x: x['enrolledScore'])
    return allEnrolls

def makeOffer(degrees, student):
    if (len(student['preferences']) == 0):
        student['offer'] == "-"
        return
    preference = student['preferences'][0]
    preference = preference.split("+")
    degree = getDegree(preference[0], degrees)
    score = student['score']
    if (len(preference) > 1):
        score += float(preference[1])
        if (score > 99.95): score = 99.95
    if (degree['places'][0] > 0):
        student["offer"][0] = degree['code']
        student["enrolledScore"][0] = score
        degree['cutoff'][0] = getEnrolledStudents([degree['code']])[0]['enrolledScore'][0]
        degree['places'][0] -= 1
    elif (degree["places"][0] == 0 and score >= degree['cutoff'][0]):
        student["offer"][0] = degree['code']
        student['enrolledScore'][0] = score
        enrolledStudents = getEnrolledStudents([degree['code']])
        removedStudent = enrolledStudents[0]
        degree['cutoff'][0] = enrolledStudents[1]['enrolledScore'][0]
        removedStudent['preferences'].pop(0)
        removedStudent['offer'][0] = "-"
        makeOffer(degrees, removedStudent)
    else:
        student['preferences'].pop(0)
        makeOffer(degrees, student)

def makeOffers(degrees, students):
    for student in students:
        makeOffer(degrees, student)

def setupDegrees():
    degrees = [line for line in csv.DictReader(open("degrees.csv"))]
    for i in range(len(degrees)):
        degree = dict(degrees[i])
        degrees[i]["places"] = [int(degree["places"])]
        degrees[i]["cutoff"] = [0]
    return sorted(degrees, key = lambda x: x['code'])

def setupStudents():
    students = [line for line in csv.DictReader(open("students.csv"))]
    for i in range(len(students)):
        student = students[i]
        students[i]["preferences"] = student["preferences"].split(";")
        students[i]["score"] = float(student["score"])
        students[i]["enrolledScore"] = [students[i]["score"]]
        students[i]["offer"] = ["-"]
    return sorted(students, key = lambda x: x['name'])

def formatDegrees(degrees):
    for i in range(len(degrees)):
        degree = degrees[i]
        degree['cutoff'] = "%.2f"%(degree['cutoff'][0])
        if (degree['cutoff'] == "0.00"): degree['cutoff'] = "-"
        degree['places'] = degree['places'][0]
        if (degree['places'] == 0): degree['vacancies'] = "N"
        else: degree["vacancies"] = "Y"
        degree.pop('places')
        degrees[i] = degree
    return sorted(degrees, key = lambda x: x['code'])

def formatStudents(students):
    for i in range(len(students)):
        student = students[i]
        student['offer'] = student['offer'][0]
        student["score"] = "%.2f"%(student["score"])
        student.pop('preferences')
        student.pop('enrolledScore')
        students[i] = student
    return sorted(students, key = lambda x: x['score'], reverse = True)

def main():
    degrees = setupDegrees()
    global students
    students = setupStudents()
    makeOffers(degrees, students)
    degrees = formatDegrees(degrees)
    students = formatStudents(students)
    writer = csv.DictWriter(sys.stdout, fieldnames = ["code","name","institution","cutoff","vacancies"], lineterminator="\n")
    print("code,name,institution,cutoff,vacancies")
    for deg in degrees:
        writer.writerow(deg)
    print("")
    writer = csv.DictWriter(sys.stdout, fieldnames = ["name","score","offer"], lineterminator="\n")
    print("name,score,offer")
    for stu in students:
        writer.writerow(stu)

main()
