import cv2
import numpy as np


def compute_entropy(img):
    # Compute the histogram of the image
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    # Compute the entropy
    hist = hist[hist != 0]
    hist = hist / hist.sum()
    entropy = -np.sum(hist * np.log2(hist))
    return entropy