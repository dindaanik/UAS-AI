# -*- coding: utf-8 -*-
"""

@author: Dinda Anik M
"""

import cv2

img = cv2.imread('dinda.jpeg')

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

x = img[:, :, 1]
cv2.imshow('image', x)
cv2.waitKey(0)