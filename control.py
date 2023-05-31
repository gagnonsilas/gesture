import gesture

class Control:

    _gesture = 0
    _trackingPoint = 0
    _lastPos = (0, 0)
    _startAction = 0
    _action = 0
    _endAction = 0

    def __init__(self, gesture, action = lambda *args: None, trackingPoint=0, startAction = lambda *args: None, endAction = lambda *args: None):
        self._gesture = gesture
        self._trackingPoint = trackingPoint
        self._action = action
        self._startAction = startAction
        self._endAction = endAction

    def update(self, hand):
        if self._gesture.check(hand):
            if self._lastPos != (0, 0):
                self._action(
                    self._lastPos.x - hand[self._trackingPoint].x,
                    self._lastPos.y - hand[self._trackingPoint].y
                    )
            else:
                self._startAction()

            self._lastPos = hand[self._trackingPoint]
        
        else: 
            self._lastPos = (0, 0)
            self._endAction()
                