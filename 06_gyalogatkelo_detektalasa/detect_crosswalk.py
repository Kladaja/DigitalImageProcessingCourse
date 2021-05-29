# Digitalis kepfeldolgozas
# Beadando feladat

import cv2
import numpy as np


def crosswalk(img_original):
    cv2.imshow('eredeti fenykep', img_original)

    # eredeti fenykep szincsatornakra bontasa
    b, g, r = cv2.split(img_original)

    blue = np.ndarray(b.shape, np.uint8)
    blue.fill(0)
    blue[b > 115] = 255

    green = np.ndarray(g.shape, np.uint8)
    green.fill(0)
    green[g > 125] = 255

    red = np.ndarray(r.shape, np.uint8)
    red.fill(0)
    red[r > 133] = 255

    rg = cv2.bitwise_and(red, green)
    rgb = cv2.bitwise_and(rg, blue)
    cv2.imshow('feher elemek szegmentalva', rgb)

    # gyalogatkelo konturjainak kivalogatasa
    _, img_thresh = cv2.threshold(rgb, 127, 255, 0)
    img_contours, img_hierarchy = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    contours_filtered = []
    for contour in range(0, len(img_contours)):
        contour_area = cv2.contourArea(img_contours[contour])

        if 500 < contour_area:
            contours_filtered.append(img_contours[contour])

    cv2.drawContours(img_original, contours_filtered, -1, (0, 0, 255), thickness=-1)

    cv2.imshow('eredmeny', img_original)
    cv2.waitKey()
    cv2.destroyAllWindows()


# kepek beolvasasa
img_1 = cv2.imread('crosswalk.jpg', cv2.IMREAD_COLOR)
img_2 = cv2.imread('crosswalk2.jpg', cv2.IMREAD_COLOR)
img_3 = cv2.imread('crosswalk3.jpg', cv2.IMREAD_COLOR)
img_4 = cv2.imread('crosswalk4.jpg', cv2.IMREAD_COLOR)
img_5 = cv2.imread('crosswalk5.jpg', cv2.IMREAD_COLOR)
img_6 = cv2.imread('crosswalk6.png', cv2.IMREAD_COLOR)

crosswalk(img_1)
crosswalk(img_2)
crosswalk(img_3)
crosswalk(img_4)
crosswalk(img_5)
crosswalk(img_6)
