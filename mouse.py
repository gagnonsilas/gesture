import pyautogui


class Mouse:
    def __init__(self, button):
        self.down = False
        self.button = button

    def release(self):
        if self.down:
            pyautogui.mouseUp(button=self.button)
            self.down = False

    def press(self):
        pyautogui.mouseDown(button=self.button)
        self.down = True


def move(x, y):
    pyautogui.move(x * 3000, y * -3000, .1)

right = Mouse('right')
left = Mouse('left')
