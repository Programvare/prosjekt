#This file handles the queue system for the app
dCourse = {}

def addToQueue(user, course):
    if course in dCourse and user not in dCourse[course]:
        dCourse.get(course).append(user)
    else:
        dCourse[course] = [user]
def removeFromQueue(course):
    if course in dCourse:
        dCourse[course].pop(0)

def getPosision(user, course):
    if course in dCourse and user in dCourse[course]:
        return dCourse[course].index(user)+1
    else:
        return 0;
