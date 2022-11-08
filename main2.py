import numpy as np

import Echographie as echo
import cv2

echo1 = echo.read("ressources/2019010A.jpg")

print(echo1)
print(echo1.imgPath)
print(echo1.width)
print(echo1.height)

img = echo1.filter(30)
cv2.imshow("wow", img)
echo1.show_with_grid(30)
cv2.imshow("wow2", echo1.img)
img2 = echo1.get_subimage(210, 180, 180, 120)
cv2.imshow("wow3", img2)
cv2.waitKey(0)


