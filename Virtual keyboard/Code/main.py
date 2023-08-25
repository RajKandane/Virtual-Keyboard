import cv2
from HandTrackingModule import HandDetector
from Utils import cornerRect
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from pynput.keyboard import Controller


class button:
    # need to add double underscores
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text

    def recOfKey(self):
        x, y = self.pos
        w, h = self.size
        return [self.pos, [x+w, (y+h)]]


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
    if rec[1][0] > point[0] > rec[0][0] and rec[1][1] > point[1] > rec[0][1]:
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


def openFile():
    global newtext
    newtext = ""
    filepath = filedialog.askopenfilename(initialdir="D:\\programs\\4th_year_project\\Virtual Keyboard Document",

                                          title="Open file okay?",
                                          filetypes=(("text files", "*.txt"),
                                                     ("all files", "*.*")))
    file = open(filepath, 'r')
    newtext = file.read()
    clip.delete("1.0", "end")
    clip.insert(END, newtext)
    file.close()


def save(newtext):
    try:
        filepath = filedialog.askopenfilename(initialdir="D:\\programs\\4th_year_project\\Virtual Keyboard Document",
                                              title="Open file okay?",
                                              filetypes=(("text files", "*.txt"),
                                                         ("all files", "*.*")))
        file = open(filepath, 'a')
        file.write('\n text added')
        file.write(newtext)
        file.close()
    except Exception:

        print("Could not write to file")
        newtext = ''

    clip.delete("1.0", "end")


win = Tk()
win.title("VIRTUAL KEYBOARD")
win.geometry("1370x750+10+10")
win.state('zoomed')
win.config(bg="#3a3b3c")

newtext = ''
capslock = True
video_path = 0
# For Browsing Videos


def browse():
    global video_path, cap
    video_path = filedialog.askopenfilename()
    cap = cv2.VideoCapture(video_path)



def live():
    global video_path, cap
    video_path = 0
    cap = cv2.VideoCapture(video_path)

# =================================================================================================================================


#Live_Button


live_btn = Button(win, height=50, width=130, text="Live", bg='#e7e6d1', fg='magenta', font=("Calibri", 14, "bold"),
                  command=lambda: live())
live_btn.place(x=600, y=10, width=150, height=25)

#Browser_button

browse_btn = Button(win, height=50, width=130, text="Browse", bg='#e7e6d1', fg='magenta', font=("Calibri", 14, "bold"),
                    command=lambda: browse())
browse_btn.place(x=750, y=10, width=150, height=25)
# =================================================================================================================================

cap = cv2.VideoCapture(video_path)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1500)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)


detector = HandDetector(detectionCon=0.2, maxHands=2)
keys = [
        ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "_", "+"],
        ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "{", "}"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";", ":", "'"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/", "<", ">"],
        ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "|"],
        ]


x = 10
y = 0
finalText = ""

keyboard = Controller()

buttonList = []

for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(button([100 * j + 25, 100 * i + 50], key))


Capslock = button([1250, 50], "CAPSLOCK", size=[185, 85])
Enter = button([1250, 150], "ENTER", size=[185, 85])
Backspace = button([1250, 250], "<---", size=[185, 85])
Space = button([1250, 350], 'SPACE', size=[185, 85])

spacial_keys = [Capslock, Enter, Backspace, Space]

label1 = Label(win, width=1500, height=580)
label1.place(x=10, y=200)

clip = Text(win, height=50, width=50, font=("Calibri", 24, "bold"), yscrollcommand=True)
clip.place(x=10, y=40, width=1500, height=150)

# =================================================================================================================================

newfilebutton = Button(win, text='File', padx=20, pady=20, bg='#e7e6d1', fg='magenta', font=(
    "Calibri", 14, "bold"), command=lambda: openFile())

newfilebutton.place(x=10, y=10, width=100, height=25)

savebutton = Button(win, text='Save', padx=20, pady=20, bg='#e7e6d1', fg='magenta', font=("Calibri", 14, "bold"),
                    command=lambda: save(newtext))
savebutton.place(x=1400, y=10, width=100, height=25)

quit_ = Button(win, text='Exit', padx=20, pady=20, bg='#e7e6d1', fg='magenta', font=("Calibri", 14, "bold"),
               command=lambda: win.destroy())

quit_.place(x=1300, y=10, width=100, height=25)

checkagain = True
pressed = button([0, 0], None, size=[0, 0])

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
                if unpressed(pressed, lmList1):
                    checkagain = True
                    pressed = button([0, 0], None, size=[0, 0])
            for i in buttonList:
                if unpressed(pressed, lmList1):
                    checkagain = True
                    pressed = button([0, 0], None, size=[0, 0])
        image = Image.fromarray(img)
        finalImage = ImageTk.PhotoImage(image)
        label1.configure(image=finalImage)
        label1.image = finalImage

    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    win.update()
