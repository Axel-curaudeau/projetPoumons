import time

import numpy as np
import Analyzer
import Image
import cv2
import Entropy

img1 = Image.read("ressources/poumons/182.jpg")

img1 = img1.filter(25)
img2 = img1.copy()

time1 = time.process_time()
img1.smoothfilter(1)
time2 = time.process_time()
img2.smoothfilter_nump(1)
time3 = time.process_time()


print("time1 : ", time2 - time1)
print("time2 : ", time3 - time2)
time4 = time.process_time()
print("time3 : ", time4 - time3)

img1.show("img1")
img2.show("img2")

"""
img_filtered_30 = img.filter(25)

intersection = []

for i in range(50, img_filtered_30.width - 50):
    if img_filtered_30.array[300, i][0] == 255 and img_filtered_30.array[300, i - 1][0] == 0:
        intersection.append((i, i + 1, "NB"))
    elif img_filtered_30.array[300, i][0] == 0 and img_filtered_30.array[300, i - 1][0] == 255:
        intersection.append((i, i + 1, "BN"))

for i in intersection:
    img_filtered_30.addLine(i[0], 298, i[0] + 1, 298, (0, 0, 255))

for i in range(1, len(intersection)):
    if intersection[i][2] == "BN" and intersection[i - 1][2] == "NB":
        xl = intersection[i - 1][0]
        xr = intersection[i][0]

img.addRectangle(xl, 300, xr - xl, -100, (0, 0, 255))
"""

Image.wait_and_close()
