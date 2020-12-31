#LEARN OPENCV in 3 HOURS-Murtaza Workshop- March 25 2020

# Chapter 7:Colour Detection

#EXAMPLE 2: Creating a trackbar function to Determine maximum and nimum values of an image

import cv2
import numpy as np

def empty():
    pass
path =("webcamdimesions.png")
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
"""
#UNIVERSAL VALUES FOR THE MASK
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)  # Max Value =180; Min Value=0
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)  
cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)   # Saturation Max Value =255
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)
"""

# DEFAULT VALUES FOR THE MASK
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)  # Max Value =180; Min Value=0
cv2.createTrackbar("Hue Max","TrackBars",19,179,empty)  
cv2.createTrackbar("Sat Min","TrackBars",110,255,empty)   # Saturation Max Value =255
cv2.createTrackbar("Sat Max","TrackBars",240,255,empty)
cv2.createTrackbar("Val Min","TrackBars",153,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


# READING OFF TRACK BAR VALUES - Change POSITION in real Time
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max","TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min","TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max","TrackBars")
    v_min = cv2.getTrackbarPos("Val Min","TrackBars")
    v_max = cv2.getTrackbarPos("Val Max","TrackBars")

    print(h_min,h_max,s_min,s_max,v_min,v_max)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])

    mask = cv2.inRange(imgHSV,lower,upper)  # gives out the filtered out BLACK &WHITEimage/s we are after
#--------------------------------------------------------------------------

    imgResult = cv2.bitwise_and(img,img,mask=mask)  # Creates a Coloured Image from the Original one


    cv2.imshow("Original",img)
    cv2.imshow("HSV",imgHSV)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result",imgResult)

    cv2.waitKey(1)


#----------------------------------------------------

# example 1: Basic detection of a image- without Refining/filtering/Raw Capture
"""
import cv2

path =("webcamdimesions.png")
img = cv2.imread(path)

imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


cv2.imshow("Original",img)

# The Detected Image
cv2.imshow("HSV",imgHSV)

cv2.waitKey(0)
"""
#------------------------------------------------------------
