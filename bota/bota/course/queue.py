#This file handles the queue system for the app
dCourse = {}

def addToQueue(course, user):
    print(dCourse)
    if(course in dCourse):
        if(user not in dCourse[course]):
            dCourse.get(course).append(user)
    else:
        dCourse[course] = [user]
def removeFromQueue(course):
    if(course in dCourse):
        dCourse[course].pop(0)

def getPosision(user, courseid):
    return dCourse[courseid].index(user)+1
