import csv
import cv2
import Analyzer
from matplotlib import pyplot as plt

RESSOURCES_PATH = "ressources/"


def generate_patient_list_txt_file():
    file = open(RESSOURCES_PATH + "Patients/BaseAnnoteeWorkBookModif.csv")
    csv_reader = csv.reader(file)
    lines = []

    for row in csv_reader:
        lines.append(row)
    file.close()
    result = []
    for i in range(len(lines)):
        sub_line = []
        for j in range(len(lines[i])):
            temp = lines[i][j].split(";")
            for k in temp:
                if len(k) != 0:
                    sub_line.append(k)
        result.append(sub_line)
    result.pop(0)
    file = open(RESSOURCES_PATH + "Patients/PatientsList.txt", "w")
    for i in result:
        for j in i:
            file.write(j)
            file.write(";")
        file.write("\n")
    file.close()


def read_patient_list_file(patient_file_path):
    patient_file = open(patient_file_path, "r")
    patient_list = patient_file.readlines()
    patient_file.close()
    result = []
    for line in patient_list:
        result.append(line.split(";"))
        result[-1].pop(-1)
    return result


def write_patient_list_file(patient_file_path, patient_list):
    patient_file = open(patient_file_path + "2", "w")
    for i in patient_list:
        for j in i:
            patient_file.write(str(j))
            patient_file.write(";")
        patient_file.write("\n")
    patient_file.close()


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


def entropy_on_all_image():
    fichier = open("entropyList-1.txt", "w")
    for i in range(322):
        image1 = cv2.imread(RESSOURCES_PATH + "poumons2/" + str(i) + ".jpg")
        analyze = Analyzer.Analyzer(image1)
        fichier.write(str(analyze.entropy(1)) + "\n")
        print(i)

def graph_entropy_all_image():
    patients_list = read_patient_list_file("ressources/Patients/PatientsList2.txt")

    Y = [int(patient[4]) for patient in patients_list]
    X = [patient[-1] for patient in patients_list]

    print(X)
    plt.scatter(Y, X)
    plt.show()

def min_color(image):
    min_color = 255
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i][j] < min_color:
                min_color = image[i][j]
    return min_color

def test_subimage_func(func, folder, folder_size, ratio_max = 3, color_min = 0, show_image=False):
    nb_error = 0
    error = False

    for i in range(folder_size):
        image = cv2.imread(folder + "/" + str(i) + ".jpg", cv2.IMREAD_GRAYSCALE)
        subimg = func(image)

        if subimg is None:
            error = True
        elif subimg.shape[0] == 0 or subimg.shape[1] == 0:
            error = True
        elif subimg.shape[0] > image.shape[0] or subimg.shape[1] > image.shape[1]:
            error = True
        elif subimg.shape[0] < 0 or subimg.shape[1] < 0:
            error = True
        elif subimg.shape[0] == image.shape[0] and subimg.shape[1] == image.shape[1]:
            error = True
        elif subimg.shape[0] > (subimg.shape[1] * ratio_max) or subimg.shape[1] > (subimg.shape[0] * ratio_max):
            error = True
        elif min_color(subimg) < color_min:
            error = True
        else:
            error = False

        if error:
            nb_error += 1
            error = False
            print("Error on image " + str(i))
            if show_image:
                cv2.imshow("image", image)
                cv2.imshow("subimg", subimg)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

    percent_correct = round((folder_size - nb_error) / folder_size * 100,1)

    print("===============================================================")
    for i in range(0, int(percent_correct / 2) + 2):
        print(" ", end="")
    print(str(percent_correct) + " % ")
    print("0%  |", end="")
    for i in range(0, int(percent_correct / 2)):
        print("█", end="")
    if percent_correct % 2 == 1:
        print("▌", end="")
    for i in range(int(percent_correct / 2), 50):
        print("-", end="")
    print("|  100 %")
    print("===============================================================")
    print("Number of error: " + str(nb_error))
    print("Number of image: " + str(folder_size))
    print("Percentage of error: " + str(nb_error / folder_size * 100) + "%")
    print("===============================================================")

