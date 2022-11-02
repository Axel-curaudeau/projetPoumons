import cv2

def read(path):
    echo = Echographie(path)
    return echo

class Echographie:
    nom = None
    ligne_pleurale_irreguliere = None
    nb_ligne_B = None
    epaississement_ligne_pleurale = None
    imgPath = None
    img = None

    def __init__(self, imgPath):
        self.imgPath = imgPath
        self.img = cv2.imread(imgPath)
        self.nom = imgPath.split("/")[-1].split(".")[0]