# Digitalis kepfeldolgozas - gyakorlat
# Elso felevkozi beadando feladat

import cv2
import numpy as np


def mouse_click(event, x, y, flags, param):
    global canvas
    global btn_down
    global size
    global color
    if event == cv2.EVENT_LBUTTONDOWN:
        btn_down = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if btn_down:
            if shape == "circle":
                cv2.circle(canvas, (x, y), size, color, -1)
            if shape == "rectangle":
                cv2.rectangle(canvas, (x, y), (x + size, y + size), color, -1)
    elif event == cv2.EVENT_LBUTTONUP:
        btn_down = False
        if shape == "circle":
            cv2.circle(canvas, (x, y), size, color, -1)
        if shape == "rectangle":
            cv2.rectangle(canvas, (x, y), (x + size, y + size), color, -1)


def keypress():
    global size
    global color
    global shape
    global key
    # szinek
    if key == ord("b"):
        color = (255, 0, 0)
    if key == ord("g"):
        color = (0, 255, 0)
    if key == ord("r"):
        color = (0, 0, 255)
    if key == ord("k"):
        color = (0, 0, 0)
    if key == ord("w"):
        color = (255, 255, 255)
    if key == ord("y"):
        color = (0, 255, 255)
    if key == ord("a"):
        color = (255, 255, 0)
    if key == ord("m"):
        color = (255, 0, 255)
    # meret
    if key == ord("+"):
        if size + 5 <= 100:
            size += 5
    if key == ord("-"):
        if size - 5 >= 5:
            size -= 5
    # alak
    if key == ord("c"):
        shape = "circle"
    if key == ord("v"):
        shape = "rectangle"
    # torles
    if key == ord("t"):
        canvas.fill(255)
    # mentes
    if key == ord("s"):
        # cv2.imwrite("canvas.png", canvas)
        cv2.imwrite("output.png", canvas)


# kepmatrix letrehozasa, feltoltese feher szinnel
canvas = np.ndarray((480, 640, 3), np.uint8)
canvas.fill(255)
cv2.imshow("canvas", canvas)

# globalis valtozok letrehozasa: egeresemenyek, meret, szin, alakzat
btn_down = False
size = 10
color = (0, 0, 255)
shape = "circle"
key = 1

cv2.setMouseCallback("canvas", mouse_click)

# tajekoztato informacio kiiratasa
print("Szin valtoztatasa:\n\tr - piros\n\tg - zold\n\tb - kek\n\tk - fekete\n\tw - feher"
      "\n\ty - sarga\n\ta - cyan\n\tm - magenta")
print("Meret valtoztatasa:\n\t+ - noveles\n\t- - csokkentes")
print("Alakzat valtoztatasa:\n\tc - kor\n\tv - negyzet")
print("Torles: t\nKep mentese: s\nKilepes: q/esc")

while True:
    cv2.imshow("canvas", canvas)
    key = cv2.waitKeyEx(1)
    # billentyulenyomasok kezelese
    keypress()
    # kilepes
    if key == 27 or key == 113:
        break

cv2.destroyAllWindows()
