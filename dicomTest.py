import numpy as np
import pydicom
from matplotlib import pyplot as plt
import cv2
import EchoTools

path = "./ressources/2019010A"

ds = pydicom.dcmread(path)

array = ds.pixel_array

width = len(array[0][0])
height = len(array[0])

heat_map = np.zeros((height, width), dtype=np.uint32)

for k in range(1, len(array)):
    heat_map += np.abs(array[k] - array[k - 1])


print(np.max(heat_map))
# convert value to 0-255
heat_map = (heat_map * 255 / np.max(heat_map)).astype(np.uint8)
print(heat_map)
cv2.imshow("heat_map", heat_map)
cv2.waitKey(0)