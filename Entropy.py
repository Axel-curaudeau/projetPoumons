import cv2
import numpy as np


def compute_entropy(img):
    """
    :param img: The input image as a numpy array.
    :return: The entropy value of the image.
    """

    ''' Compute the histogram of the image to calculate the probabilities. '''
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])

    hist = hist[hist != 0]
    hist = hist / hist.sum()
    entropy = -np.sum(hist * np.log2(hist))
    return entropy
