import numpy as np

import Image
import cv2

img1 = Image.read("ressources/2019010A.jpg")

print(img1)
print(img1.path)
print(img1.width)
print(img1.height)

img2 = img1.filter(30)
cv2.imshow("filter", img2.array)
img1.show_with_grid(30)
cv2.imshow("de base", img1.array)
img3 = img1.get_subimage(210, 180, 180, 120)
cv2.imshow("sub image", img3.array)
cv2.waitKey(0)


