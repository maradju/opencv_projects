# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 09:56:00 2020

@author: Marija
"""
#Homework No 5 - Iris

#importing required libraries
import numpy as np
import cv2
import polarTransform

#loading the image in grayscale

img = cv2.imread('Iris1.png', 0)

#detecting circles
#cv2.HoughCircles (image, circles, method, dp, minDist[, param1[, param2[ , minRadius[, maxRadius]]]]])
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 17, 250, 299)
circles = np.uint16(np.around(circles))


for i in circles[0,:]:
        #lines -  outer circle
        cv2.circle(img,(i[0], i[1]), i[2], (0,255,0), 3)
        
        #lines - inner circle
        cv2.circle(img,(i[0], i[1]), 99, (0,255,0), 3)

#I will extract some values from the circles
# (x,y) represents the center of the pupil
x = circles[0][0][0]
y = circles[0][0][1]
# r represents the radius of the whole eye
r = circles[0][0][2]*2

#Now we know the center of the circle and the radius we can use method linearPolar
#cv2.linearPolar(src, center, maxRadius, flags[, dst])

image = cv2.imread('Iris1.png', 0)
float_img = image.astype(np.float32)
value = np.sqrt(((float_img.shape[0]/2.0)**2.0)+((float_img.shape[1]/2.0)**2.0))
polar_image=cv2.linearPolar(float_img, (x,y), r, cv2.WARP_FILL_OUTLIERS)
polar_image = polar_image.astype(np.uint8)
height, width = polar_image.shape
s2 = polar_image[:, width // 2:]


cv2.imshow('image', img)
cv2.imwrite('texture.png',s2 )
cv2.waitKey(5000)
cv2.destroyAllWindows()
