import cv2
import numpy as np

img1 = "123.png"
img2 = "long_circle.png"

BLEND_X = 0.1
BLEND_Y = 0.05
BLEND_OPAQUE = 0.5
img_bg = cv2.imread(img1)
img_fg = cv2.imread(img2)
result = cv2.addWeighted(img_bg, BLEND_OPAQUE, img_fg, BLEND_OPAQUE,0)
img_fg = cv2.resize(img_fg,(800,600))
cv2.imwrite("apc.png", img_fg)
cv2.imshow('res',img_fg)

cv2.waitKey(0)