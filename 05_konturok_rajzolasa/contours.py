# Digitalis kepfeldolgozas
# Otodik felevkozi beadando feladat

import cv2

# kep beolvasasa
img = cv2.imread('car_numberplate_rs.jpg', cv2.IMREAD_COLOR)
# cv2.imshow('original img', img)

img_gray = cv2.imread('car_numberplate_rs.jpg', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('gray', img_gray)

# adaptiv kuszoboles vegrehajtasa
img_thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 15, 45)
# cv2.imshow('tresh', img_thresh)

# konturkereses a kuszobolt kepen
img_contours, img_hierarchy = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# 200 es 800 pixel kozotti kozrezart teruletu konturok hozzaadasa egy listahoz
img_contours_filtered = []
for cntrIndx in range(0, len(img_contours)):
    countour_area = cv2.contourArea(img_contours[cntrIndx])

    # 200-as ertek helyett 160-at vettem, mert ezzel jobb megoldast adott
    # if 200 < countour_area < 800:
    if 160 < countour_area < 800:
        img_contours_filtered.append(img_contours[cntrIndx])

# megfelelo meretu konturok teruleteinek berajzolasa
cv2.drawContours(img, img_contours_filtered, -1, (0, 255, 255), 3, cv2.LINE_4)
cv2.imshow('contours', img)

cv2.imwrite('output.png', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
