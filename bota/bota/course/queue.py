# This file handles the queue system for the app
dCourse = {}


def add_to_queue(user, course):
    if course in dCourse and user not in dCourse[course]:
        dCourse.get(course).append(user)
    else:
        dCourse[course] = [user]


def rm_from_queue(course):
    if course in dCourse and (dCourse.get(course)):
        dCourse.get(course).pop(0)


def get_position(user, course):
    if course in dCourse and user in dCourse[course]:
        return dCourse[course].index(user)
    else:
        return 0


def get_next(course):
    if course in dCourse and dCourse.get(course):
        return dCourse.get(course)[0]
    return ""


def user_in_queue(user, course):
    if course in dCourse and user in dCourse[course]:
        return True
    return False


def get_length(course):
    if course in dCourse:
        return len(dCourse[course])
    return 0


def leave_queue(course, user):
    if course in dCourse and user in dCourse[course]:
        position = get_position(user, course)
        dCourse.get(course).pop(position)
