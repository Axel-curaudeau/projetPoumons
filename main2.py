import numpy as np

import Analyzer
import Image
import cv2
import Entropy

img = Image.read("ressources/poumons/182.jpg")

img_filtered_30 = img.filter(25)

intersection = []

for i in range(50, img_filtered_30.width - 50):
    if img_filtered_30.array[300,i][0] == 255 and img_filtered_30.array[300,i-1][0] == 0:
        intersection.append((i,i+1,"NB"))
    elif img_filtered_30.array[300,i][0] == 0 and img_filtered_30.array[300,i-1][0] == 255:
        intersection.append((i,i+1,"BN"))

for i in intersection:
    img_filtered_30.addLine(i[0], 298, i[0]+1, 298, (0, 0, 255))

for i in range(1, len(intersection)):
    if intersection[i][2] == "BN" and intersection[i-1][2] == "NB":
        xl = intersection[i-1][0]
        xr = intersection[i][0]

img.addRectangle(xl, 300, xr-xl, -100, (0, 0, 255))

img_filtered_30.show("img_filtered_30")
img.show("img")

Image.wait_and_close()
