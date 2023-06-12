import cv2
from HandTrackingModule import HandDetector
from time import sleep
from Utils import cornerRect
from pynput.keyboard import Controller

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=.8, maxHands=2)

keys = [
        ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "_", "+"],
        ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "|"],
        ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "{", "}"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";", ":", "'"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/", "<", ">"],
        [" ", "\b"]
]
spacial_keys = ["SPACE", "BACKSPACE", "SHIFT", "ENTER"]

finalText = ""

keyboard = Controller()


def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cornerRect(img, (button.pos[0], button.pos[1],
                         button.size[0], button.size[0]), 20, rt=0)
        cv2.rectangle(img, button.pos, (x + w, y + h), (255, 204, 255), 2)
        cv2.putText(img, button.text, (x + 20, y + 65),
                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 255), 4)
    return img


# def drawAll(img, buttonList):
#     imgNew = np.zeros_like(img, np.uint8)
#     for button in buttonList:
#         x, y = button.pos
#         cvzone.cornerRect(imgNew, (button.pos[0], button.pos[1], button.size[0], button.size[1]), 20, rt=0)
#         cv2.rectangle(imgNew, button.pos, (x+button.size[0], y+button.size[1]), (255, 0, 255), cv2.FILLED)
#         cv2.putText(imgNew, button.text, (x+20, y+65), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)

#     out = img.copy()
#     alpha = .5
#     mask = imgNew.astype(bool)
#     print(mask.shape)
#     out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]
#     return out

class Button():
    def __init__(self, pos, text, size=[80, 80]):
        self.pos = pos
        self.size = size
        self.text = text




buttonList = []

for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 50, 100 * i + 50], key))

#for k in range(len(spacial_keys)):
 #   for f, key in enumerate(spacial_keys[k]):
  #      buttonList.append(Button([100 * f + 50, 100 * k + 50], spacial_keys))

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)
    img = drawAll(img, buttonList)

    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # list of 21 landmarks
        bbox1 = hand1["bbox"]  # bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Hand Type "Left" or "Right"

        fingers2 = detector.fingersUp(hand1)

        if len(hands) == 2:
            # Hand 2
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmark points
            bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
            centerPoint2 = hand2['center']  # center of the hand cx,cy
            handType2 = hand2["type"]  # Hand Type "Left" or "Right"

            fingers2 = detector.fingersUp(hand2)


        for button in buttonList:
            x, y = button.pos
            w, h = button.size

            if x < lmList1[8][0] < x + w and y < lmList1[8][1] < y + h:
                cv2.rectangle(img, button.pos, (x + w, y + h), (175, 0, 175), cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 65),
                            cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)

                l, _, _ = detector.findDistance(lmList1[8], lmList1[12], img)
                img2 = detector.findHands(img)
                print(l)

                if l < 45:
                    keyboard.press(button.text)
                    cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 65),
                                cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                    finalText += button.text
                    sleep(0.13)

    cv2.rectangle(img, (60, 635), (1250, 700), (175, 0, 175), cv2.FILLED)
    cv2.putText(img, finalText, (80, 700),
                cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)

    cv2.imshow("Virtual keyboard", img)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()


cv2.destroyAllWindows()