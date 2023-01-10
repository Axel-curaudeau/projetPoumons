import cv2
import Entropy
import EchoTools
import Tools
from matplotlib import pyplot as plt

#Tools.test_subimage_func(EchoTools.sub_image, "ressources/poumons2", folder_size=321, ratio_max=10, color_min=1, show_image=False)

patient_list = Tools.read_patient_list_file("ressources/Patients/PatientsList2.txt")
csvfile = open("ressources/Patients/PatientsList2.csv", "w")
for patient in patient_list:
    csvfile.write(patient[4] + ";" + patient[-1] + "\n")

csvfile.close()

