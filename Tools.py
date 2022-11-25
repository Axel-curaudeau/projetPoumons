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
    error = None
    error_type = [0 for i in range(7)]


    for i in range(folder_size):
        image = cv2.imread(folder + "/" + str(i) + ".jpg", cv2.IMREAD_GRAYSCALE)
        subimg = func(image)

        if subimg is None:
            error = "No subimage found"
            error_type[0] += 1
        elif subimg.shape[0] == 0 or subimg.shape[1] == 0:
            error = "Subimage has a dimension of 0"
            error_type[1] += 1
        elif subimg.shape[0] > image.shape[0] or subimg.shape[1] > image.shape[1]:
            error = "Subimage is bigger than the original image"
            error_type[2] += 1
        elif subimg.shape[0] < 0 or subimg.shape[1] < 0:
            error = "Subimage has a negative dimension"
            error_type[3] += 1
        elif subimg.shape[0] == image.shape[0] and subimg.shape[1] == image.shape[1]:
            error = "Subimage is the same size as the original image"
            error_type[4] += 1
        elif subimg.shape[0] > (subimg.shape[1] * ratio_max) or subimg.shape[1] > (subimg.shape[0] * ratio_max):
            error = "Subimage has a ratio bigger than " + str(ratio_max)
            error_type[5] += 1
        elif min_color(subimg) < color_min:
            error = "Subimage has a color lower than " + str(color_min)
            error_type[6] += 1
        else:
            error = False

        if error:
            nb_error += 1
            print("Error on image " + str(i) + ": " + error)
            if show_image:
                cv2.imshow("Image " + str(i) + " - " + error, image)
                cv2.imshow("subimg", subimg)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            error = False

    percent_correct = round((folder_size - nb_error) / folder_size * 100,1)

    line_size = 66
    print("")
    print("╔══════════════════════ Correct Image Rate ══════════════════════╗")

    print("║    ", end="")
    for i in range(0, int(percent_correct / 2.1) + 2):
        print(" ", end="")
    print("\033[1;31m" + str(percent_correct) + " % " + "\033[1;0m", end="")
    for i in range(int(percent_correct / 2.1) + len(str(percent_correct)+ " %"), line_size-9):
        print(" ", end="")
    print("║")

    nb_char = 0
    print("║ 0 % |", end="")
    nb_char += 7
    for i in range(0, int(percent_correct / 2)):
        print("█", end="")
        nb_char += 1
    if percent_correct % 2 == 1:
        print("▌", end="")
        nb_char += 1
    for i in range(nb_char, 57):
        print("-", end="")
    if percent_correct % 2 == 0 and percent_correct != 100 and percent_correct != 0:
        print("-", end="")
    print("| 100 % ║")

    print("╠════════════════════════ Global  Report ════════════════════════╣")
    print("║ Number of error: \033[1;31m" + str(nb_error) + "\033[1;0m", end="")
    for i in range(0, line_size - 20 - len(str(nb_error))):
        print(" ", end="")
    print("║")
    print("║ Number of image: " + str(folder_size), end="")
    for i in range(0, line_size - 20 - len(str(folder_size))):
        print(" ", end="")
    print("║")
    print("╠═════════════════════════ Error Report ═════════════════════════╣")
    print("║ No subimage found: \033[1;31m" + str(error_type[0]) + "\033[1;0m", end="")
    for i in range(0, line_size - 22 - len(str(error_type[0]))):
        print(" ", end="")
    print("║")
    print("║ Subimage has a dimension of 0: \033[1;31m" + str(error_type[1]) + "\033[1;0m", end="")
    for i in range(0, line_size - 34 - len(str(error_type[1]))):
        print(" ", end="")
    print("║")
    print("║ Subimage is bigger than the original image: \033[1;31m" + str(error_type[2]) + "\033[1;0m", end="")
    for i in range(0, line_size - 47 - len(str(error_type[2]))):
        print(" ", end="")
    print("║")
    print("║ Subimage has a negative dimension: \033[1;31m" + str(error_type[3]) + "\033[1;0m", end="")
    for i in range(0, line_size - 38 - len(str(error_type[3]))):
        print(" ", end="")
    print("║")
    print("║ Subimage is the same size as the original image: \033[1;31m" + str(error_type[4]) + "\033[1;0m", end="")
    for i in range(0, line_size - 52 - len(str(error_type[4]))):
        print(" ", end="")
    print("║")

    nb_char = 0
    print("║ Subimage has a ratio bigger than " + str(ratio_max) + ": \033[1;31m" + str(error_type[5]) + "\033[1;0m", end="")
    nb_char += 38 + len(str(ratio_max)) + len(str(error_type[5]))
    for i in range(nb_char, line_size):
        print(" ", end="")
    print("║")

    nb_char = 0
    print("║ Subimage has a color lower than " + str(color_min) + ": \033[1;31m" + str(error_type[6]) + "\033[1;0m", end="")
    nb_char += 39 + len(str(color_min)) + len(str(error_type[6]))
    for i in range(nb_char, line_size + 2):
        print(" ", end="")
    print("║")
    print("╚════════════════════════════════════════════════════════════════╝")

