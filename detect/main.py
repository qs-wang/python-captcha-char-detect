# coding:utf8
import sys
import cv2
import numpy as np
 
def preprocess(gray):
    sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, ksize = 3)
    ret, binary = cv2.threshold(sobel, 0, 255, cv2.THRESH_OTSU+cv2.THRESH_BINARY)
 
    # tune here for character detection size
    element1 = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 5))
    element2 = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 5))
 
    dilation = cv2.dilate(binary, element2, iterations = 1)
    erosion = cv2.erode(dilation, element1, iterations = 1)
    dilation2 = cv2.dilate(erosion, element2, iterations = 3)
 
    # following are for debugging
    # cv2.imwrite("binary.png", binary)
    # cv2.imwrite("dilation.png", dilation)
    # cv2.imwrite("erosion.png", erosion)
    # cv2.imwrite("dilation2.png", dilation2)
 
    return dilation2
 
 
def findTextRegion(img):
    region = []
 
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
 
    for i in range(len(contours)):
        cnt = contours[i]
        area = cv2.contourArea(cnt) 
 
        # ignore too small area
        if(area < 100):
            continue
 
        # epsilon = 0.001 * cv2.arcLength(cnt, True)
        # approx = cv2.approxPolyDP(cnt, epsilon, True)
 
        rect = cv2.minAreaRect(cnt)

        box = cv2.boxPoints(rect)
        box = np.int0(box)
 
        height = abs(box[0][1] - box[2][1])
        width = abs(box[0][0] - box[2][0])
 
        # ignore too small box
        if width < 10:
            continue
 
        region.append(box)
 
    return region
 
 
def detectCharInCaptcha(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
    dilation = preprocess(gray)
 
    region = findTextRegion(dilation)
 
    cut_id = 0
    for box in region:
        # following code for saving the dected area to be separate images
        # img_save = img[box[0][1]:box[2][1], box[0][0] : box[2][0]]
        # if len(img_save) != 0:
        #     filename = "./tmp/" + str(cut_id) + ".png"
        #     cv2.imwrite(filename, img_save)
        #     cut_id+=1

        cv2.drawContours(img, [box], 0, (0, 255, 0), 2)
 
    cv2.namedWindow("img", cv2.WINDOW_NORMAL)
    cv2.imshow("img", img)
 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
 
if __name__ == '__main__':
    imagePath = sys.argv[1]
    img = cv2.imread(imagePath)
    detectCharInCaptcha(img)