import Tools
import cv2
import EchoTools
import Entropy
from matplotlib import pyplot as plt


def graph_sub_image():
    """
    Show the graph with entropy value of all images using sub_image function, in function of their number of B lines.
    """
    list_entropy = []
    numbers_b_lines = []
    ressources_path = "./ressources/Patients/"
    patient_list = Tools.read_patient_list_file("ressources/Patients/PatientsList2.txt")
    for patient in patient_list:
        path = Tools.get_echo_path(patient)
        image = cv2.imread(ressources_path + path, cv2.IMREAD_GRAYSCALE)
        sub_image = EchoTools.sub_image(image)
        entropy = Entropy.compute_entropy(sub_image)
        if entropy > 2:
            list_entropy.append(entropy)
            numbers_b_lines.append(int(patient[4]))
    print("Nombre de valeur : ", len(list_entropy))
    plt.scatter(numbers_b_lines, list_entropy)
    plt.show()


def graph_entropy_all_image(patient_list_file_path):
    """
    Show the graph with entropy value of all images, in function of their number of B lines.
    """
    patients_list = Tools.read_patient_list_file(patient_list_file_path)

    Y = [int(patient[4]) for patient in patients_list]
    X = [float(patient[-1]) for patient in patients_list]

    print("Nombre de valeur :", len(X))
    plt.scatter(Y, X)
    plt.show()

def graph_sub_image_slide_entropy(path, show_image=False):
    """
    Show one graph for all image using the slide_entropy function.
    """
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    entropy = EchoTools.slide_entropy(image, 10, "horizontal")
    entropy_vert = EchoTools.slide_entropy(image, 10, "vertical")
    plt.plot(entropy)
    plt.plot(entropy_vert)
    cv2.imshow(path, image)
    plt.show()
    cv2.waitKey(0)