import os.path
import cv2
from matplotlib import pyplot as plt

import Analyzer
#import matplotlib.pyplot as plt

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


def read_patient_list_file(patient_file_path):
    patient_file = open(patient_file_path, "r")
    patient_list = patient_file.readlines()
    patient_file.close()
    result = []
    for line in patient_list:
        result.append(line.split(";"))
        result[-1].pop(-1)
    return result

def get_echo_path(patient):
    num_patient = patient[0][len(patient[0]) - 2:]
    path = ""
    if int(num_patient) <= 8:
        path = "0"
    path += patient[0] + "/"
    if int(num_patient) <= 10:
        path += "1"
    else:
        path += "10"
    path += num_patient + patient[1] + "/" + patient[2] + ".jpg"
    return path


# --------- Main ---------

# entropy_test()
patients_list = read_patient_list_file("ressources/Patients/PatientsList.txt")
for patient in patients_list:
    path = get_echo_path(patient)
    print(path, os.path.exists("ressources/Patients/" + path))

X = [i for i in range(len(patients_list))]
Y = [patient[4] for patient in patients_list]

plt.scatter(X, Y)
plt.show()