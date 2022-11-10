import numpy as np

import Analyzer
import Image
import cv2
import Entropy

img = Image.read("ressources/2019010A.jpg")

img1 = img.get_subimage(233, 185, 135, 75)
img2 = img.get_subimage(260, 187, 82, 71)
img3 = img.get_subimage(275, 150, 51, 106)

img.addRectangle(233, 185, 135, 75, (0, 0, 255))
img.addRectangle(260, 187, 82, 71, (0, 255, 0))
img.addRectangle(275, 150, 51, 106, (255, 0, 0))

an1 = Analyzer.Analyzer(img1.array)
an2 = Analyzer.Analyzer(img2.array)
an3 = Analyzer.Analyzer(img3.array)

print("Entropy Rouge : ", Entropy.compute_entropy(img1.array))
print("Entropy Vert : ", Entropy.compute_entropy(img2.array))
print("Entropy Bleu : ", Entropy.compute_entropy(img3.array))

cv2.imshow("img", img.array)

cv2.waitKey(0)
cv2.destroyAllWindows()


