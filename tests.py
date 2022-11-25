import unittest
import Entropy
import cv2

def test_entropy():
    img = cv2.imread("ressources/entro_0,64.png", cv2.IMREAD_GRAYSCALE)
    print(Entropy.compute_entropy(img))
    print(img)
    cv2.imshow("img", img)
    cv2.waitKey(0)
    assert Entropy.compute_entropy(img) == 0.64
