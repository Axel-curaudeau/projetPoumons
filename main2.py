import cv2
import Entropy
import EchoTools
from matplotlib import pyplot as plt

img = cv2.imread("ressources/Patients/03Patient 1DR03/103M0/2019010A.jpg", cv2.IMREAD_GRAYSCALE)

subimg = EchoTools.sub_image(img)
list_e_vert = EchoTools.slide_entropy(subimg, 20, "vertical")
list_e_hor = EchoTools.slide_entropy(subimg, 20, "horizontal")

plt.plot(list_e_vert)
plt.plot(list_e_hor)
plt.show()

cv2.imshow("img", img)
cv2.imshow("subimg", subimg)

cv2.waitKey(0)
cv2.destroyAllWindows()
