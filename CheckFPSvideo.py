# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 10:46:18 2017

@author: kilicm
"""
"""
This script will check how many frames per second from video.
Ex. 1 second video captures 29 frames.
"""


import cv2
if __name__ == '__main__' :
 
    video = cv2.VideoCapture("mt.mp4");
     
    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
     
    if int(major_ver)  < 3 :
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
        print ("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else :
        fps = video.get(cv2.CAP_PROP_FPS)
        print ("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
     
video.release();