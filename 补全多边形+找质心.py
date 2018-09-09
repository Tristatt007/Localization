import cv2
import numpy as np
#import argparse
#import imutils
import random as rng
im = cv2.imread('D:\\lalalalala\\documents\\beautifulLife\\TestSamples\\figures\\3.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)#参数是原图和转色类型，输出是灰度图
ret, thresh = cv2.threshold(imgray,127,255,cv2.THRESH_BINARY)#参数是灰度图、阈值、高于阈值时被赋予的新值、低于阈值时被赋予的新值

image,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#参数是阈值化后的图，索引方式。输出是图像，轮廓和层级结构。
#img = cv2.drawContours(im,contours,-1,(0,255,0),3)#参数是原始图像，轮廓，轮廓的索引（颜色厚度等）
#cv2.imshow('contours',image)
#hull = cv2.convexHull(img)
#im_end = cv2.imshow('img',hull)
#image和thresh都是白底黑线图，contours是数列和他的格式。
 # Find the convex hull object for each contour
print(contours)
hull_list = []
for i in range(len(contours)):
    hull = cv2.convexHull(contours[i])
    hull_list.append(hull)
    # Draw contours + hull results
    drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), dtype=np.uint8)
for i in range(len(contours)):
    color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
    cv2.drawContours(drawing, contours, i, color)
    cv2.drawContours(drawing, hull_list, i,color)
#print(contours)

for i in range(1,len(contours)):
    M = cv2.moments(contours[i])
    if M["m00"] != 0:   
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0
    cv2.circle(drawing, (cX, cY), 3, (255, 255, 255), -1)

  #  cv2.putText(drawing, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

cv2.imshow('Contours', drawing)


cv2.waitKey(0)
cv2.destroyAllWindows()