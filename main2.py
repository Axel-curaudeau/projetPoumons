import cv2
import Entropy
import EchoTools
import Tools
from matplotlib import pyplot as plt

Tools.test_subimage_func(EchoTools.sub_image, "ressources/poumons2", folder_size=321, ratio_max=10, color_min=1, show_image=False)


cv2.waitKey(0)
cv2.destroyAllWindows()
