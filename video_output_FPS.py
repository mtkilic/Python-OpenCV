# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 11:07:43 2017

@author: kilicm
"""

"""
This script takes video as input and outputs Frames Per Second. 
Approximally there is more than 20 pictures(frames) per second. 
"""
import cv2
cap = cv2.VideoCapture('mt.mp4')
count = 0
while cap.isOpened():
    ret,frame = cap.read()
    cv2.imshow('window-name',frame)
    cv2.imwrite("frame%d.jpg" % count, frame)
    count = count + 1
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


cap.release()
cap.destroyAllWindows()
