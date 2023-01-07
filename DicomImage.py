import cv2
import pydicom
import Entropy
from EchoTools import smooth


class DicomImage:
    name = ""
    path = ""
    B_lines = 0

    def __init__(self, path, name):
        self.path = path
        self.name = name

    def image_array(self):
        """
        :return: The image as a numpy array.
        """
        return pydicom.dcmread(self.path).pixel_array

    def entropy_list(self):
        """
        :return: The liste of entropy values for each image of the dicom file.
        """
        entropy_list = []
        images = self.image_array()
        for image in images:
            entropy_value = Entropy.compute_entropy(image)
            entropy_list.append(entropy_value)
        return entropy_list


def sub_image(image):
    """
    :param image: the image as a numpy array.
    :return: a sub image of the image as a numpy array, avoiding the shadows of the ribs.
    """

    intersection = []
    image_filtered = smooth(image, 30, 7)
    ''' Smooth the image to avoid noise and find a clear demarcation between the shadow and the image. '''

    width = len(image_filtered[0])

    for i in range(50, width - 50):
        if image_filtered[300, i] == 255 and image_filtered[300, i - 1] == 0:
            intersection.append((i, i + 1, "NB"))
        elif image_filtered[300, i] == 0 and image_filtered[300, i - 1] == 255:
            intersection.append((i, i + 1, "BN"))

    for i in intersection:
        cv2.line(image_filtered, (i[0], 298), (i[0] + 10, 298), 160, 2)
        # image_filtered.addLine(i[0], 298, i[0] + 1, 298, (0, 0, 255))

    xl = 0
    xr = 1
    for i in range(1, len(intersection)):
        if intersection[i][2] == "BN" and intersection[i - 1][2] == "NB":
            xl = intersection[i - 1][0]
            xr = intersection[i][0]

    # cv2.rectangle(image, (xl, 300), (xr, 200), 155, 2)
    # image.addRectangle(xl, 300, xr - xl, -100, (0, 0, 255))

    # cv2.imshow("filter", image_filtered)
    # print(xl, " ", xr)
    return image[200:300, xl:xr]
