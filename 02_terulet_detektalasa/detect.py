# Digitális képfeldolgozás
# Második félévközi beadandó feladat

import cv2
import numpy as np

img = cv2.imread('hk_flower.jpg', cv2.IMREAD_COLOR)  # fénykép betöltése
# cv2.imshow('eredeti', img)  # eredeti fénykép megjelenítése


# fehér virágszirmok detektálása
b, g, r = cv2.split(img)  # csatornákra bontás

blue_th = np.ndarray(b.shape, np.uint8)
blue_th.fill(0)
blue_th[b > 153] = 255
# cv2.imshow('blue', blue_th)

green_th = np.ndarray(g.shape, np.uint8)
green_th.fill(0)
green_th[g > 152] = 255
# cv2.imshow('green', green_th)

red_th = np.ndarray(r.shape, np.uint8)
red_th.fill(0)
red_th[r > 154] = 255
# 155-as érték esetén 0 lesz a norma, az abszolút különbség szemléltetése végett hagytam 154-en
# cv2.imshow('red', red_th)

mask_th = cv2.bitwise_and(red_th, green_th)
result_th = cv2.bitwise_and(mask_th, blue_th)
cv2.imshow('szirmok detektalva', result_th)  # eredmény megjelenítése


# eredménymaszk használata az eredeti képen
result_bgr = cv2.merge([cv2.bitwise_and(b, result_th), cv2.bitwise_and(result_th, g), cv2.bitwise_and(result_th, r)])
cv2.imwrite('res_segm.png', result_bgr)  # kép mentése külön fájlba
cv2.imshow('eredmenymaszk az eredeti kepen', result_bgr)


# eredmény összehasonlítása egy előzetesen elkészülttel
img2 = cv2.imread('hk_flower_szirom.png', cv2.IMREAD_GRAYSCALE)  # előzetes eredménykép betöltése
# cv2.imshow('szirmok2', img2)

diff = cv2.absdiff(result_th, img2)  # abszolút különbség kiszámítása
cv2.imshow('abszolut kulonbseg', diff)  # abszolút különbség megjelenítése

norm = cv2.norm(diff / 255, cv2.NORM_L1)
print("L1 norma: ", norm)

cv2.waitKey(0)  # várakozás billentyű lenyomására
cv2.destroyAllWindows()  # ablakok bezárása
