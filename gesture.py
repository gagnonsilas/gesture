import utils

class Gesture:
    _landmarks = 0
    _distances = 0

    def __init__(self, landmarks, distances):
        self._landmarks = landmarks
        self._distances = distances

    def check(self, hand):
        for id, (p1, p2) in enumerate(self._landmarks):
            if(utils.dist(hand[p1], hand[p2]) > self._distances[id] or (self._distances[id] < 0) and utils.dist(hand[p1], hand[p2]) < -self._distances[id]):
                return False
        return True

