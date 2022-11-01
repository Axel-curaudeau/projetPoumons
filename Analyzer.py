import cv2
import numpy as np


class Analyzer:
    STEP = 20

    CUT_NB = 3

    A_X = 0.0
    A_Y = 208.0
    B_X = 298.0
    B_Y = 0.0

    C_X = 0.0
    C_Y = 473.0
    D_X = 300.0
    D_Y = 680.0

    def __int__(self, image_path):
        self.Image = cv2.imread(image_path)

    def __init__(self, image):
        self.Image = image

    def proba(self, color_step):
        proba_value = [0 for _ in range(0, 256, color_step)]
        for x in range(self.Image.shape[0]):
            for y in range(self.Image.shape[1]):
                if self.is_inside(x, y):
                    proba_value[int(self.Image[x, y][0] / color_step)] += 1
        for x in range(len(proba_value)):
            proba_value[x] = proba_value[x] / (self.Image.shape[0] * self.Image.shape[1])
        return proba_value

    def entropy(self, color_step):
        entropy_value = 0
        proba_value = self.proba(color_step)
        for value in range(len(proba_value)):
            if proba_value[value] != 0:
                entropy_value += proba_value[value] \
                                  * np.log2(1 / proba_value[value])
        return entropy_value

    def is_inside(self, x, y):
        """
        Check if a point is inside the echographie

        Parameters
        ----------
        x : int
            x coordinate of the point
        y : int
            y coordinate of the point

        Returns
        -------
        bool
            True if the point is inside the echographie shape, False otherwise
        """

        # Left side
        if (self.B_Y - self.A_Y) / (self.B_X - self.A_X) * x + self.A_Y >= y:
            return False

        # Right side
        if (self.D_Y - self.C_Y) / (self.D_X - self.C_X) * x + self.C_Y <= y:
            return False

        # Top side
        if -0.00239 * y * y + 1.62919 * y - 235 >= x:
            return False

        # Bottom side
        if -0.00091 * y * y + 0.61765 * y + 300 <= x:
            return False
        return True
