import cv2
import mediapipe as mp
import time
import gesture
import control
import pyautogui
import mouse
import key

import utils


RIGHT, LEFT = utils.RIGHT, utils.LEFT
pyautogui.PAUSE = 0.001
pyautogui.FAILSAFE = False

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,
                      max_num_hands=2,
                      min_detection_confidence=0.7,
                      min_tracking_confidence=0.6)
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0




while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    # print(results.multi_handedness)


    if results.multi_hand_landmarks and results.multi_handedness:
        for idh, hand_handedness in enumerate(results.multi_handedness):
            for handLms in results.multi_hand_landmarks:
                for idl, lm in enumerate(handLms.landmark):#Show Joints
                    h, w, c = img.shape
                    cx, cy, cz = int(lm.x * w), int(lm.y * h), lm.z * -20
                    cv2.circle(img, (cx, cy), 3, (255 * cz, 0, 255 * cz), cv2.FILLED)
                    cv2.putText(img, str(idl), (cx, cy), cv2.FONT_HERSHEY_PLAIN, 1, (255, 170, 20), 1)
            for i in control.MouseControls.listed:
                i.update(results.multi_hand_landmarks[idh].landmark, hand_handedness.classification[0].index)
            # for i in control.ControlScemeA.listed:
            #     i.update(results.multi_hand_landmarks[idh].landmark, hand_handedness.classification[0].index)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
