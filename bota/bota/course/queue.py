from .models import Queue
# This file handles the queue system for the app

def save_to_queue(course_id, queue_array):
    comma = ","
    queue_string = comma.join(queue_array)

    try:
        queue_object = Queue.objects.get(course_id=course_id)
        queue_object.queue = queue_string

    except Queue.DoesNotExist:
        queue_object = Queue(course_id=course_id, queue=queue_string)

    queue_object.save()


def get_queue(course_id):
    try:
        queue_string = Queue.objects.get(course_id=course_id).queue
        if queue_string == "":
            return []
        queue_array = queue_string.split(',')
        return queue_array
    except Queue.DoesNotExist:
        return []


def add_to_queue(user, course):
    queue = get_queue(course)
    if user.username not in queue:
        queue.append(user.username)
    save_to_queue(course, queue)


def rm_from_queue(course):
    queue = get_queue(course)
    if not queue.__len__() == 0:
        queue.pop(0)
        save_to_queue(course, queue)


def get_position(user, course):
    queue = get_queue(course)
    if user.username in queue:
        return queue.index(user.username)
    return 0


def get_next(course):
    queue = get_queue(course)
    if not queue.__len__() == 0:
        return queue[0]
    return None


def user_in_queue(user, course):
    queue = get_queue(course)
    return user.username in queue


def get_length(course):
    queue = get_queue(course)
    return queue.__len__()


def leave_queue(course, user):
    queue = get_queue(course)
    if user.username in queue:
        queue.remove(user.username)
        save_to_queue(course, queue)
