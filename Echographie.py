import cv2

def read(path):
    echo = Echographie(path)
    return echo

def echo_from_img(img):
    echo = Echographie(img)
    return echo

class Echographie:
    nom = None
    ligne_pleurale_irreguliere = None
    nb_ligne_B = None
    epaississement_ligne_pleurale = None
    imgPath = None
    img = None
    width = None
    height = None

    def __init__(self, imgPath):
        self.imgPath = imgPath
        self.img = cv2.imread(imgPath)
        self.nom = imgPath.split("/")[-1].split(".")[0]
        self.width = self.img.shape[1]
        self.height = self.img.shape[0]

    def __str__(self):
        return self.nom

    def get_subimage(self, x, y, w, h):
        return self.img[int(y):int(y+h), int(x):int(x+w)]

    def show_with_grid(self, step):
        img_temp = self.img.copy()
        for i in range(0, self.height, step):
            for j in range(0, self.width,):
                img_temp[i, j] = [0, 0, 255]
        for i in range(0, self.width, step):
            for j in range(0, self.height):
                img_temp[j, i] = [0, 0, 255]
        cv2.imshow("grid", img_temp)
        cv2.waitKey(0)

    def filter(self, level):
        img_temp = self.img.copy()
        for i in range(0, self.height):
            for j in range(0, self.width):
                if img_temp[i, j][0] < level:
                    img_temp[i, j] = [0, 0, 0]
                else:
                    img_temp[i, j] = [255, 255, 255]
        return img_temp
