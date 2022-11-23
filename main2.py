import cv2
import Entropy
from matplotlib import pyplot as plt

img = cv2.imread("ressources/poumons/171.jpg", cv2.IMREAD_GRAYSCALE)

def slide_entropy(img, slide_width):
    list_entropy = []
    for x in range(0, img.shape[1]-slide_width):
        list_entropy.append(Entropy.compute_entropy(img[:,x:x + slide_width]))
    return list_entropy

elist = slide_entropy(img, 10)
print(elist)
x_list = [i for i in range(len(elist))]
plt.plot(x_list, elist)
plt.show()

cv2.imshow("img", img)


cv2.waitKey(0)
cv2.destroyAllWindows()
