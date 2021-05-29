# Digitalis kepfeldolgozas
# Negyedik felevkozi beadando feladat

import cv2
import numpy as np


def hsv_segment(interval_H, interval_S, interval_V, wndtitle):
    global imgHSV

    minHSV = np.array([interval_H[0], interval_S[0], interval_V[0]])
    maxHSV = np.array([interval_H[1], interval_S[1], interval_V[1]])
    segmented = cv2.inRange(imgHSV, minHSV, maxHSV)
    # cv2.imshow(wndtitle, segmented)

    return segmented


# szines kep beolvasasa
img_colored = cv2.imread('PalPant_800.jpg', cv2.IMREAD_COLOR)
# cv2.imshow('original img', img)

# maszk letrehozasa a tengerhez
blurred = cv2.GaussianBlur(img_colored, (5, 5), sigmaX=2.0, sigmaY=2.0)
imgHSV = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
img_bg_color = hsv_segment((100, 120), (3, 129), (139, 197), 'segmented')
img_bg_bw = cv2.bitwise_not(img_bg_color)

# az eredmeny szines reszenek letrehozasa
b, g, r = cv2.split(img_colored)
b_and = cv2.bitwise_and(b, img_bg_color)
g_and = cv2.bitwise_and(g, img_bg_color)
r_and = cv2.bitwise_and(r, img_bg_color)
img_colored_result = cv2.merge([b_and, g_and, r_and])

# az eredmeny szurkearnyalatos reszenek letrehozasa
img_gray = cv2.cvtColor(img_colored, cv2.COLOR_BGR2GRAY)
img_gray_bw = cv2.bitwise_and(img_bg_bw, img_gray)
img_gray_result = cv2.cvtColor(img_gray_bw, cv2.COLOR_GRAY2BGR)

# az eredmeny letrehozasa
result = cv2.bitwise_or(img_gray_result, img_colored_result)
cv2.imshow('result', result)
cv2.imwrite('output.jpg', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
