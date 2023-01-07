import Tools
import cv2
import EchoTools
import Entropy
from matplotlib import pyplot as plt


def graph_sub_image(filepath):
    """
    Show the graph with entropy value of all images using sub_image function, in function of their number of B lines.
    It will calculate the entropy of a sub-image of the original image, in order to avoid the shadows caused by the ribs.
    :param filepath: The path of a formated file containing the list of patients, and their entropy value. The file
    must be formated like this:
        "patient_name;exam_name;image_name;pleural_line_irregularity;number_of_B_lines;CPI_score"
    """

    list_entropy = []
    numbers_b_lines = []
    ressources_path = "./ressources/Patients/"
    patient_list = Tools.read_patient_list_file(filepath)

    for patient in patient_list:
        path = Tools.get_echo_path(patient)
        image = cv2.imread(ressources_path + path, cv2.IMREAD_GRAYSCALE)
        sub_image = EchoTools.sub_image(image)
        entropy = Entropy.compute_entropy(sub_image)
        if entropy > 6:
            list_entropy.append(entropy)
            numbers_b_lines.append(int(patient[4]))

    print("Nombre de valeur : ", len(list_entropy))
    plt.scatter(numbers_b_lines, list_entropy)
    plt.xlabel("Nombre de lignes B")
    plt.ylabel("Entropie")
    plt.show()


def graph_entropy_all_image(patient_list_file_path):
    """
    Show the graph with entropy value of all images, in function of their number of B lines.
    :param: patient_list_file_path: The path of a formatted file containing the list of patients,
    and their entropy value. The file must be formatted like this:
    "patient_name;exam_name;image_name;pleural_line_irregularity;number_of_B_lines;CPI_score;entropy_value"
    """
    patients_list = Tools.read_patient_list_file(patient_list_file_path)

    Y = [int(patient[4]) for patient in patients_list]
    X = [float(patient[-1]) for patient in patients_list]

    print("Nombre de valeur :", len(X))
    fig, ax = plt.subplots()
    ax.scatter(Y, X)
    ax.set_xlabel("Nombre de lignes B")
    ax.set_ylabel("Entropie")
    plt.show()


def graph_sub_image_slide_entropy(path):
    """
    :param path:
    :return:
    """
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    entropy = EchoTools.slide_entropy(image, 10, "horizontal")
    entropy_vert = EchoTools.slide_entropy(image, 10, "vertical")
    fig, ax = plt.subplots()
    ax.plot(entropy)
    ax.plot(entropy_vert)
    ax.legend(["rectangle horizontal", "rectangle vertical"])
    cv2.imshow(path, image)
    plt.show()
    cv2.waitKey(0)
