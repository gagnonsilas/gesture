import key
import utils
import mouse
import gesture
keys = key.Keys

pinch = gesture.Pinches
LEFT, RIGHT = utils.LEFT, utils.RIGHT


class Control:

    _gesture = 0
    _trackingPoint = 0
    _lastPos = (0, 0)
    _startAction = 0
    _action = 0
    _endAction = 0

    def __init__(self, gesture, handedness, action = lambda *args: None, trackingPoint=0, startAction = lambda *args: None, endAction = lambda *args: None):
        """

        @rtype: object
        """
        self._gesture = gesture
        self._trackingPoint = trackingPoint
        self._action = action
        self._startAction = startAction
        self._endAction = endAction
        self._handedness = handedness

    def update(self, hand, handedness):
        if self._handedness == handedness:
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

class MouseControls:
    RIGHT, LEFT = utils.RIGHT, utils.LEFT
    LMID = utils.LandmarkIds
    # MouseControl
    leftClick = Control(
        pinch.index,
        RIGHT,
        startAction=lambda *args: mouse.left.press(),
        endAction=lambda *args: mouse.left.release()
    )

    rightClick = Control(
        pinch.middle,
        RIGHT,
        startAction=lambda *args: mouse.right.press(),
        endAction=lambda *args: mouse.right.release()
    )

    mouseMove = Control(
        pinch.ring,
        RIGHT,
        lambda x, y: mouse.move(x, y)
    )

    listed = [leftClick,rightClick, mouseMove]

class KeyControl(Control):

    def __init__(self, gesture, handedness, key):
        super().__init__(
            gesture,
            handedness,
            startAction=lambda *args: key.press(),
            endAction=lambda *args: key.release()
        )

class ControlScemeA:
    wPress = KeyControl(pinch.middle, LEFT, keys.w)
    aPress = KeyControl(pinch.ring, LEFT, keys.a)
    sPress = KeyControl(pinch.pinky, LEFT, keys.s)
    dPress = KeyControl(pinch.index, LEFT, keys.d)

    listed = [wPress, aPress, sPress, dPress]



# #KeyPresses    WASD
# wPress = control.Control(
#     pinch.middle,
#     LEFT,
#     startAction=lambda *args: keys.w.press(),
#     endAction=lambda *args: keys.w.release()
# )
#
# aPress = control.Control(
#     pinch.ring,
#     LEFT,
#     startAction=lambda *args: keys.a.press(),
#     endAction=lambda *args: keys.a.release()
# )
#
# sPress = control.Control(
#     gesture.Gesture([(LMID.PINKY_TIP, LMID.THUMB_MID)], [0.08]),
#     LEFT,
#     startAction=lambda *args: keys.s.press(),
#     endAction=lambda *args: keys.s.release()
# )
#
# dPress = control.Control(
#     gesture.Gesture([(LMID.INDEX_TIP, LMID.THUMB_MID)], [0.08]),
#     LEFT,
#     startAction=lambda *args: keys.d.press(),
#     endAction=lambda *args: keys.d.release()
# )
# spacePress = control.Control(
#     gesture.Gesture([(LMID.THUMB_TIP, LMID.INDEX_LOW)], [0.05]),
#     LEFT,
#     startAction=lambda *args: spaceKey.press(),
#     endAction=lambda *args: spaceKey.release()
# )
#
# #KeyPresses    QWER
# qPress = control.Control(
#     gesture.Gesture([(LMID.PINKY_TIP, LMID.THUMB_MID)], [0.08]),
#     LEFT,
#     startAction=lambda *args: qKey.press(),
#     endAction=lambda *args: qKey.release()
# )
#
# wPress = control.Control(
#     gesture.Gesture([(LMID.RING_TIP, LMID.THUMB_MID)], [0.08]),
#     LEFT,
#     startAction=lambda *args: wKey.press(),
#     endAction=lambda *args: wKey.release()
# )
#
# ePress = control.Control(
#     gesture.Gesture([(LMID.MIDDLE_TIP, LMID.THUMB_MID)], [0.08]),
#     LEFT,
#     startAction=lambda *args: eKey.press(),
#     endAction=lambda *args: eKey.release()
# )
#
# rPress = control.Control(
#     gesture.Gesture([(LMID.INDEX_TIP, LMID.THUMB_MID)], [0.08]),
#     LEFT,
#     startAction=lambda *args: rKey.press(),
#     endAction=lambda *args: rKey.release()
# )