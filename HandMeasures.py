#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 09:30:24 2020

@author: marija
"""

# import the necessary packages
import imutils
import cv2
import math
import numpy as np
# load the image, convert it to grayscale, and blur it slightly
image = cv2.imread("index.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
# threshold the image, then perform a series of erosions +
# dilations to remove any small regions of noise
thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
thresh = cv2.erode(thresh, None, iterations=2)
thresh = cv2.dilate(thresh, None, iterations=2)
# find contours in thresholded image, then grab the largest
# one
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
c = max(cnts, key=cv2.contourArea)

# determine the most extreme points along the contour
extLeft = tuple(c[c[:, :, 0].argmin()][0])
extRight = tuple(c[c[:, :, 0].argmax()][0])
extTop = tuple(c[c[:, :, 1].argmin()][0])
extBot = tuple(c[c[:, :, 1].argmax()][0])

#determine center point of the conture
m = cv2.moments(cnts[2])
cx = int(m["m10"] / m["m00"])
cy = int(m["m01"] / m["m00"])

cv2.circle(image, (cx, cy), 1, (0, 0, 255), 8)

# draw the outline of the object, then draw each of the
# extreme points, where the left-most is red, right-most
# is green, top-most is blue, and bottom-most is teal
cv2.drawContours(image, [c], -1, (0, 255, 255), 2)
cv2.circle(image, extLeft, 8, (0, 0, 255), -1)
cv2.circle(image, extRight, 8, (0, 255, 0), -1)
cv2.circle(image, extTop, 8, (255, 0, 0), -1)
cv2.circle(image, extBot, 8, (255, 255, 0), -1)

#draw line
line = cv2.line(image, (cx, cy), extTop, (0, 255, 0), thickness=4)
dist = math.sqrt( (cx - cy)**2 + (extTop[0] - extTop[1])**2 )
print("Size of the line is: " + str(dist) )
# show the output image
cv2.imshow("Image", image)
cv2.waitKey(0)