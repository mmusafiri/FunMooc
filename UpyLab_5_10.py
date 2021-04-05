def dupliques(checklist):

    for n in range(len(checklist)-1):
        if checklist.count(checklist[n]) > 1:
            return True
    return False
