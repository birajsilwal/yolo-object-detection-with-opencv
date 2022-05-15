import math

import cv2
import cvzone
import numpy as np
from cvzone.HandTrackingModule import HandDetector

# webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 470)

# Detect the hand using hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Find Function
# x is the raw distance got from the distance of the landmark 5 and 7
# y is the value in cm, measured with the tape
x = [300, 245, 200, 170, 145, 130, 112, 103, 93, 87, 80, 75, 70, 67, 62, 59, 57]
y = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
# finding the coff for the relation between x and y
coff = np.polyfit(x, y, 2)  # y = Ax^2 + Bx + C

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        # list of landmarks of the hand
        lmList = hands[0]['lmList']
        bounding_box_x, bounding_box_y, bounding_box_w, bounding_box_h = hands[0]['bbox']
        # find the distance between landmark point 5 and 7
        # see MediaPipe website for more reference
        lm_five_x1, lm_five_y1, _ = lmList[5]
        lm_seven_x2, lm_seven_y2, _ = lmList[17]

        # finding the distance between the landmark 5 and 7
        distance = int(math.sqrt((lm_seven_y2 - lm_five_y1) ** 2
                                 + (lm_seven_x2 - lm_five_x1) ** 2))

        # based on these values, we can estimate how far the object is
        A, B, C = coff
        distance_cm = int(A * distance ** 2 + B * distance + C)
        print(distance_cm)
        cvzone.putTextRect(img, f'{distance_cm} cm', (bounding_box_x + 10, bounding_box_y - 15))
        cv2.rectangle(img, (bounding_box_x, bounding_box_y),
                      (bounding_box_x + bounding_box_w, bounding_box_y + bounding_box_h), (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
