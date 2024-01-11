#!/usr/bin/python3
'''working with lockboxes in python
'''

def canUnlockAll(boxes):
    if not boxes or not boxes[0]:
        return False

    n = len(boxes)
    keys = set(boxes[0])

    for i in range(1, n):
        if i not in keys:
            return False

        keys.update(boxes[i])

    return True
