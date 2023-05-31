import cv2
import mediapipe as mp
import time
import math
import gesture
import control
import pyautogui

pyautogui.PAUSE = 0.001
pyautogui.FAILSAFE = False

cap = cv2.VideoCapture(1)

mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,
                      max_num_hands=1,
                      min_detection_confidence=0.8,
                      min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

leftClick = control.Control(
        gesture.Gesture([(4, 8)], [0.035]), 
        startAction= lambda *args : pyautogui.mouseDown(button='left'),
        endAction= lambda *args : pyautogui.mouseUp(button='left')
        )
rightClick = control.Control(
        gesture.Gesture([(4, 12)], [0.035]), 
        startAction= lambda *args : pyautogui.mouseDown(button='right'),
        endAction= lambda *args : pyautogui.mouseUp(button='right')
        )
mouseControl = control.Control(gesture.Gesture([(16, 0)], [0.15]), lambda x, y: pyautogui.move(x * 4000, y * -4000))

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy, cz = int(lm.x *w), int(lm.y*h), lm.z * -20
                cv2.circle(img, (cx,cy), 3, (255 * cz,0,255 * cz), cv2.FILLED)
                cv2.putText(img, str(id), (cx, cy), cv2.FONT_HERSHEY_PLAIN, 1, (255, 170, 20), 1)

            leftClick.update(handLms.landmark)
            rightClick.update(handLms.landmark)
            mouseControl.update(handLms.landmark)
            
            # mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

    # cv2.imshow("Image", img)
    cv2.waitKey(1)