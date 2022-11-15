import os.path
import cv2
from matplotlib import pyplot as plt

import Analyzer
import Image

RESSOURCES_PATH = "ressources/"


def cut_image(img, nb_cut):
    image_list = []
    x = 0
    y = 0
    cutted_image_width = int(img.shape[0] / nb_cut)
    cutted_image_height = int(img.shape[1] / nb_cut)
    # print(cutted_image_height, cutted_image_width)
    for i in range(1, nb_cut + 1):
        for j in range(1, nb_cut + 1):
            print(x, (i * cutted_image_width), y, (j * cutted_image_height))
            image_list.append(img[x: (i * cutted_image_width),
                                  y: (j * cutted_image_height)])

            y = j * cutted_image_height
        x = i * cutted_image_width
        y = 0
    return image_list


def entropy_test():
    fichier = open("entropyList-1.txt", "w")
    for i in range(322):
        image1 = cv2.imread(RESSOURCES_PATH + "poumons2/" + str(i) + ".jpg")
        analyze = Analyzer.Analyzer(image1)
        fichier.write(str(analyze.entropy(1)) + "\n")
        print(i)


# --------- Main ---------

# entropy_test()
'''
patients_list = read_patient_list_file("ressources/Patients/PatientsList2.txt")

Y = [int(patient[4]) for patient in patients_list]
X = [patient[-1] for patient in patients_list]

print(X)
plt.scatter(Y, X)
plt.show()
'''

img = Image.read("ressources/2019010A.jpg")
img.show("base")
for i in range(1, 10):
    smoothImg = img.smoothfilter(i)
    smoothImg.show("smooth" + str(i))

Image.wait_and_close()
