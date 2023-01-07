import os
import cv2
import Exam


class Patient:
    name = ""
    path = ""
    list_of_exams = []

    def __init__(self, patient_name: str, patient_path: str):
        self.name = patient_name
        self.path = patient_path
        self.list_of_exams = []
        dir_list = os.listdir(self.path)
        for Exam_dir in dir_list:
            self.list_of_exams.append(Exam.Exam(Exam_dir, self.path + "/" + Exam_dir))

    def read_image(self):
        """
        Read the image of the patient.
        :return: The image of the patient.
        """
        return cv2.imread(self.path, cv2.IMREAD_GRAYSCALE)


def search_all_patient(directory_path):
    patient_list = []
    dirlist1 = os.listdir(directory_path)
    for directory in dirlist1:
        if os.path.isdir(directory_path + "/" + directory) and directory.__contains__("Patient"):
            patient_list.append(Patient(directory, directory_path + "/" + directory))
    return patient_list
