import cv2
import time
import os
import matplotlib.pyplot as plt
import HandTracking as htm


wCam, hCam = 640, 480

cap = cv2.VideoCapture(-1)
cap.set(3, wCam)
cap.set(4, hCam)

folder = "./images"
myList = os.listdir(folder)
myList.sort()
print(myList)

overlayList = []


for image in myList:
    img = cv2.imread(folder + "/" + image)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, dsize=(200,200))
    overlayList.append(img)


print(len(overlayList))

pTime = 0

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20] # dedão, indicador, médio, anelar, mindinho respectivamente

while True:
    success, img = cap.read()
    img= cv2.flip(img, 1)

    img = detector.findHands(img)

    lmList = detector.findPosition(img, draw=False)
    #print(lmList)

    if len(lmList) != 0:
        fingers = []
        

        #index finger open

        #        50             100 -- OPen
        #       100              50 -- Closed

        # if lmList[8][2] < lmList[6][2]:
        #     print("Index Finger Open")

        #Dedão

        if lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        # quatro dedos
        for id in range(1,5):
            # if open append 1, else 0
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
            
        totalFingers = fingers.count(1)
        print(totalFingers)

        h, w, c = overlayList[totalFingers-1].shape
        # limit of the heigth and the width
        img[0:h, 0:w] = overlayList[totalFingers-1]

        cv2.rectangle(img, (20,225), (170, 425), (0,255,0), cv2.FILLED)
        cv2.putText(img, str(totalFingers), (45,375), cv2.FONT_HERSHEY_PLAIN,
                    10, (255,0,0), 25)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, f"FPS: {int(fps)}", (400, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255,0,0), 3)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)
