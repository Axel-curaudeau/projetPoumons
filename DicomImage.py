import pydicom

import Entropy


class DicomImage:
    name = ""
    path = ""
    B_lines = 0

    def __init__(self, path, name):
        self.path = path
        self.name = name

    def ImageArray(self):
        return pydicom.dcmread(self.path).pixel_array

    def EntropyList(self):
        entropy_list = []
        images = self.ImageArray()
        for image in images:
            entropy_value = Entropy.compute_entropy(image)
            entropy_list.append(entropy_value)
        return entropy_list

