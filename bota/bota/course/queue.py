#This file handles the queue system for the app
dCourse = {}

def addToQueue(user, course):
    if course in dCourse and user not in dCourse[course]:
        dCourse.get(course).append(user)
    else:
        dCourse[course] = [user]
def removeFromQueue(course):
    if course in dCourse and (dCourse.get(course)):
        dCourse.get(course).pop(0)

def getPosision(user, course):
    if course in dCourse and user in dCourse[course]:
        return dCourse[course].index(user)
    else:
        return 0;
def getNext(course):
    if(course in dCourse and dCourse.get(course)):
        return dCourse.get(course)[0]
    return ""
def userInQueue(user, course):
    if course in dCourse and user in dCourse[course]:
        return True
    return False