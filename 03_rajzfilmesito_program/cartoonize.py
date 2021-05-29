# Digitalis kepfeldolgozas
# Harmadik felevkozi beadando feladat

import cv2


def cartoonize(original_img, line, blur):
    # homogenebb kep elokeszitese:
    # median szures vegrehajtasa
    median_img = cv2.medianBlur(original_img, blur)
    cv2.imshow('blurred img', median_img)

    # elkep elokeszitese:
    # elkereses Canny eldetektorral
    gaussian_img = cv2.GaussianBlur(median_img, (5, 5), 2.0)
    canny_img = cv2.Canny(gaussian_img, 200, 700, None, 5, True)
    # cv2.imshow('canny img', canny_img)

    # elek megvastagitasa morfologiai dilatacioval
    struct_element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (line, line))
    canny_img_dilate = cv2.dilate(canny_img, struct_element)
    cv2.imshow('outline', cv2.bitwise_not(canny_img_dilate))

    # vegeredmeny eloallitasa:
    # elek helyen fekete szinnel helyettesitjuk a kepeket a medianszurt kepen
    # kep csatornakra bontasa
    b, g, r = cv2.split(median_img)

    # elkep negaltjaval logikai ES muvelet vegrehajtasa a szincsatornakon
    canny_img_neg = cv2.bitwise_not(canny_img_dilate)
    b_and = cv2.bitwise_and(b, canny_img_neg)
    g_and = cv2.bitwise_and(g, canny_img_neg)
    r_and = cv2.bitwise_and(r, canny_img_neg)

    # eredmenycsatornak egyesitese
    result = cv2.merge([b_and, g_and, r_and])
    cv2.imshow('result', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return result



# szines kep beolvasasa:
img = cv2.imread('input.jpg', cv2.IMREAD_COLOR)

one = cartoonize(img, 3, 7)
two = cartoonize(img, 1, 3)
three = cartoonize(img, 5, 15)

cv2.imwrite('output.jpg', two)
