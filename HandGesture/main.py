# import OpenCV for machine trainings
# cvzone for HandTracking module :

import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)  # by default , it draws the Left and right hand and shows it on screen

    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]       # List of 21 points of our hand
        bbox = hand1["bbox"]            # Bounding Box shows the x,y,w,h (dimensions)
        handType1 = hand1["type"]        # hand Type i.e. left or right
        centerPoint1 = hand1["center"]

        if len(hands) == 2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]       # List of 21 points of our hand
            bbox2 = hand2["bbox"]            # Bounding Box shows the x,y,w,h (dimensions)
            centerPoint2 = hand2["center"]
            length, info, img = detector.findDistance(centerPoint1, centerPoint2, img)
            print(length)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

