
# Reccoment friend by adding user id, 

def reccomend_friend(user_id, friendships):
    exclude = set()
    exclude.add(user_id)
    queue = [user_id]
    friendLevels = checkFriends(exclude, queue, friendships, level=0, lastOfLevel=user_id, friendLevels={}, levelStop=2)
    suggestions = set()
    for i in friendLevels.keys():
        if i not in {0, 1}:
            suggestions = (suggestions|friendLevels[i])
    return suggestions


# goes through the queue, and for each item in queue adds their friends to the queue
# level stop allows control of how deep we go
def checkFriends(exclude, userQueue, friendships, level=1, lastOfLevel=0, friendLevels={}, levelStop = -1):
    # Return If level stop has been reached
    if level == levelStop+1:
        return friendLevels
    # create new level entry
    if level not in friendLevels.keys():
        friendLevels[level] = set()

    # Pop the next element in the queue
    try:
        friend = userQueue.pop(0)
    except IndexError as e:
        return friendLevels

    # Add current friend to the correct level
    friendLevels[level].add(friend)
    # Check if we're on the last of the current level, if we are we want to get the last el of the next level and increment the level
    if lastOfLevel == friend:
        level += 1
        lastOfLevel = getLast(friendships[friend],exclude)
    
    # Cycle through the current friends friend's and add them to the queue if they're not in exclude ie not already processed
    for i in friendships[friend]:
        if i not in exclude:
            exclude.add(i)
            userQueue.append(i)

    # this call processes the next item in the queue
    checkFriends(exclude, userQueue, friendships, level, lastOfLevel, friendLevels, levelStop)
    return friendLevels

def getLast(set, exclude):
    lastEl = None
    for i in set:
        if i not in exclude:
            lastEl = i
    return lastEl


friendships = {
    1: {3, 2, 4},
    2: {1, 5},
    3: {1, 5, 6},
    4: {1, 7, 8},
    5: {2, 3, 10},
    6: {3},
    7: {4},
    8: {4, 9},
    9: {5, 8},
    10: {5}
}

user_id = 1


rec = reccomend_friend(user_id, friendships)
print(rec)
