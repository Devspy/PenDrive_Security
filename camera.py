#!/usr/bin/python36

import cv2
import os

camera = cv2.VideoCapture(0)
path = '/root/Desktop/project/photo'
for i in range(10):
	return_value, image = camera.read()
	cv2.imwrite(os.path.join(path,'opencv'+str(i)+'.png'), image)
del(camera)
