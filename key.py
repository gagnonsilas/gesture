import pyautogui
class Key:
    def __init__(self, button):
        self.down = False
        self.button = button

    def press(self):
        if not self.down:
            pyautogui.keyDown(self.button)
            self.down = True

    def release(self):
        if self.down:
            pyautogui.keyUp(self.button)
            self.down = False

class Keys:
    w = Key('w')
    a = Key('a')
    d = Key('d')
    s = Key('s')
    q = Key('q')
    e = Key('e')
    r = Key('r')
    spaceKey = Key('space')