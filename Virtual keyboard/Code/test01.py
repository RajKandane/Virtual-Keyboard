import cv2
from HandTrackingModule import HandDetector
from Utils import cornerRect
from time import sleep
import mediapipe
import numpy as np
import cvzone
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from pynput.keyboard import Controller

class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text
    def recOfKey(self):
        x, y = self.pos
        w, h = self.size
        return [self.pos, [x + w, (y + h)]]

global newtext
global capslock

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


def isInRectangle(rec, point):
    if (rec[1][0] > point[0] > rec[0][0] and rec[1][1] > point[1] > rec[0][1]):
        return True
    else:
        return False

def isPressed(b, lmList1):
    if isInRectangle(b.recOfKey(), lmList1[8][:2]) and isInRectangle(b.recOfKey(), lmList1[12][:2]):
        return True
    else:
        return False

def unpressed(b, lmList1):
    if isInRectangle(b.recOfKey(), lmList1[8][:2]) and isInRectangle(b.recOfKey(), lmList1[12][:2]):
        return False
    else:
        return True



def drawSpecial(img, spacial_keys):
    for button in spacial_keys:
        x, y = button.pos
        w, h = button.size
        cornerRect(img, (button.pos[0], button.pos[1],
                         button.size[0], button.size[0]), 20, rt=0)
        cv2.rectangle(img, button.pos, (x + w, (y + h)), (255, 204, 255), 2)
        cv2.putText(img, button.text, (x + 20, (y + 65)),
                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 4)
    return img

win = Tk()
win.title("VIRTUAL KEYBOARD")
win.geometry("1370x750+10+10")
win.state('zoomed')
win.config(bg="#3a3b3c")
newtext = ''
capslock = True
video_path = 0

cap = cv2.VideoCapture(video_path)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1500)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)


detector = HandDetector(detectionCon=0.2, maxHands=2)

#
# keys = [
#         ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
#         ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
#         ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
#         ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]
#         ]
#

#detector = HandDetector(detectionCon=.8, maxHands=2)


keys = [
        ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "_", "+"],
        ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "{", "}"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";", ":", "'"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/", "<", ">"],
        ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "|"],
        ]


x = 10
y = 0
#spacial_keys = ["SPACE", "BACKSPACE", "SHIFT", "ENTER"]

finalText = ""

keyboard = Controller()

buttonList = []

for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 25, 100 * i + 50], key))


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



# Capslock = Button([1050, 50], "CAPSLOCK", size=[185, 85])
# Enter = Button([1050, 150], "ENTER", size=[185, 85])
# Backspace = Button([1050, 250], "<---", size=[185, 85])
# Space = Button([1050, 350], 'SPACE', size=[185, 85])




Capslock = Button([1250, 50], "CAPSLOCK", size=[185, 85])
Enter = Button([1250, 150], "ENTER", size=[185, 85])
Backspace = Button([1250, 250], "<---", size=[185, 85])
Space = Button([1250, 350], 'SPACE', size=[185, 85])

spacial_keys = [Capslock, Enter, Backspace, Space]

label1 = Label(win, width=1500, height=580)
label1.place(x=10, y=200)

clip = Text(win, height=5, width=20, yscrollcommand=True)
clip.place(x=10, y=40, width=1500, height=150)
checkagain = True
pressed = Button([0, 0], None, size=[0, 0])





while True:
    success, img = cap.read()
    if success:
        img = cv2.resize(img, (1500, 580))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.flip(img, 1)
        hands, img = detector.findHands(img, flipType=False)
        drawSpecial(img, spacial_keys)
        drawAll(img, buttonList)
        if hands:
            hand1 = hands[0]
            lmList1 = hand1["lmList"]  # List of 21 Landmark points
            if isPressed(Capslock, lmList1) and checkagain:
                if capslock:
                    capslock = False
                else:
                    capslock = True
                checkagain = False
                pressed = Capslock
            elif isPressed(Enter, lmList1) and checkagain:
                newtext += '\n'
                clip.insert(END, '\n')
                checkagain = False
                pressed = Enter
            elif isPressed(Backspace, lmList1) and checkagain:
                newtext = newtext[:-1]
                clip.delete('1.0', "end")
                clip.insert(END, newtext)
                checkagain = False
                pressed = Backspace
            elif isPressed(Space, lmList1) and checkagain:
                newtext = ' '
                clip.insert(END, ' ')
                checkagain = False
                pressed = Space
            else:
                for i in buttonList:
                    if isPressed(i, lmList1) and checkagain:
                        if capslock:
                            newtext += i.text
                            clip.insert(END, i.text)
                        else:
                            newtext += i.text.lower()
                            clip.insert(END, i.text.lower())
                        checkagain = False
                        pressed = i
            for i in spacial_keys:
                if unpressed(pressed , lmList1):
                    checkagain = True
                    pressed = Button([0, 0], None, size=[0, 0])
            for i in buttonList:
                if unpressed(pressed, lmList1):
                    checkagain = True
                    pressed = Button([0, 0], None, size=[0, 0])

            # for button in buttonList:
            #     x, y = button.pos
            #     w, h = button.size
            #
            #     if x < lmList1[8][0] < x + w and y < lmList1[8][1] < y + h:
            #         cv2.rectangle(img, button.pos, (x + w, y + h), (175, 0, 175), cv2.FILLED)
            #         cv2.putText(img, button.text, (x + 20, y + 65),
            #                     cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
            #
            #         l, _, _ = detector.findDistance(lmList1[8], lmList1[12], img)
            #         img2 = detector.findHands(img)
            #         print(l)
            #
            #         if l < 55:
            #             keyboard.press(button.text)
            #             cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
            #             cv2.putText(img, button.text, (x + 20, y + 65),
            #                         cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
            #             finalText += button.text
            #             sleep(0.13)


        image = Image.fromarray(img)
        finalImage = ImageTk.PhotoImage(image)
        label1.configure(image=finalImage)
        label1.image = finalImage
    #cv2.waitKey(20)
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    win.update()