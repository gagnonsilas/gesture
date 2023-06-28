import utils

LMID = utils.LandmarkIds

tipToTipDistance = .08


class Gesture:
    _landmarks = 0
    _distances = 0

    def __init__(self, landmarks, distances):
        self._landmarks = landmarks
        self._distances = distances

    def check(self, hand):
        for id, (p1, p2) in enumerate(self._landmarks):
            if utils.dist(hand[p1], hand[p2]) > self._distances[id] or (self._distances[id] < 0) and utils.dist(
                    hand[p1], hand[p2]) < -self._distances[id]:
                return False
        return True


class Pinches:
    index = Gesture([(LMID.INDEX_TIP, LMID.THUMB_MID)], [0.08])
    middle = Gesture([(LMID.MIDDLE_TIP, LMID.THUMB_MID)], [0.08])
    ring = Gesture([(LMID.RING_TIP, LMID.THUMB_MID)], [0.08])
    pinky = Gesture([(LMID.PINKY_TIP, LMID.THUMB_MID)], [0.08])

class Curls:
    index = Gesture([(LMID.INDEX_TIP, LMID.INDEX_LOW)], [0.08])
    middle = Gesture([(LMID.MIDDLE_TIP, LMID.MIDDLE_LOW)], [0.08])
    ring = Gesture([(LMID.RING_TIP, LMID.RING_LOW)], [0.08])
    pinky = Gesture([(LMID.PINKY_TIP, LMID.PINKY_LOW)], [0.08])
    thumb = Gesture([(LMID.THUMB_TIP, LMID.THUMB_LOW)], [0.08])
