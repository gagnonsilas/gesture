import math

RIGHT = 0
LEFT = 1
def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2)


class LandmarkIds:
    WRIST = 0
    THUMB_LOW = 1
    THUMB_MID = 2
    THUMB_HIGH = 3
    THUMB_TIP = 4
    INDEX_LOW = 5
    INDEX_MID = 6
    INDEX_HIGH = 7
    INDEX_TIP = 8
    MIDDLE_LOW = 9
    MIDDLE_MID = 10
    MIDDLE_HIGH = 11
    MIDDLE_TIP = 12
    RING_LOW = 13
    RING_MID = 14
    RING_HIGH = 15
    RING_TIP = 16
    PINKY_LOW = 17
    PINKY_MID = 18
    PINKY_HIGH = 19
    PINKY_TIP = 20
