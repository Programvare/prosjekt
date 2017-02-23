#This file handles the queue system for the app
dCourse = {}

def addToQueue(user, course):
    if course in dCourse and user not in dCourse[course]:
        dCourse.get(course).append(user)
    else:
        dCourse[course] = [user]
def removeFromQueue(course):
    print(dCourse.get(course, None))
    if course in dCourse and (dCourse.get(course) is not None):
        print(dCourse.get(course, None))
        dCourse.get(course).pop(0)
        print(dCourse.get(course, None))

def getPosision(user, course):
    if course in dCourse and user in dCourse[course]:
        return dCourse[course].index(user)+1
    else:
        return 0;
def getNext(course):
    if(course in dCourse and dCourse.get(course) is not None):
        return dCourse.get(course)[0]
    return "Ingen i kø"