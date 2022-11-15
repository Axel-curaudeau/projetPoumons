import cv2
import numpy as np


def read(path):
    echo = Image(path)
    return echo


def echo_from_img(img):
    echo = Image(img)
    return echo


def wait_and_close():
    cv2.waitKey(0)
    cv2.destroyAllWindows()


class Image:
    nom = None
    path = None
    array = None
    width = None
    height = None

    def __init__(self, img_path):
        self.path = img_path
        self.array = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        self.nom = img_path.split("/")[-1].split(".")[0]
        self.width = self.array.shape[1]
        self.height = self.array.shape[0]

    def __str__(self):
        return self.nom

    def get_subimage(self, x, y, w, h):
        new_image = self.copy()
        new_image.array = new_image.array[int(y):int(y + h), int(x):int(x + w)]
        return new_image

    def show_with_grid(self, step):
        img_temp = self.array.copy()
        for i in range(0, self.height, step):
            for j in range(0, self.width, ):
                img_temp[i, j] = [0, 0, 255]
        for i in range(0, self.width, step):
            for j in range(0, self.height):
                img_temp[j, i] = [0, 0, 255]
        cv2.imshow("grid", img_temp)

    def filter(self, level):
        echo_temp = self.copy()
        for i in range(0, self.height):
            for j in range(0, self.width):
                if echo_temp.array[i, j] < level:
                    echo_temp.array[i, j] = 0
                else:
                    echo_temp.array[i, j] = 255
        return echo_temp

    def smoothfilter(self, nb):
        for i in range(nb):
            img_temp = self.array.copy()
            for x in range(1, self.width - 1):
                for y in range(1, self.height - 1):
                    sum = int(self.array[y - 1, x - 1]) + int(self.array[y - 1, x]) + int(
                        self.array[y - 1, x + 1]) + int(self.array[y, x - 1]) + int(self.array[y, x]) + int(
                        self.array[y, x + 1]) + int(self.array[y + 1, x - 1]) + int(
                        self.array[y + 1, x]) + int(self.array[y + 1, x + 1])
                    if sum < 1100:
                        img_temp[y, x] = 0
                    else:
                        img_temp[y, x] = 255
            self.array = img_temp
        return self

    def smoothfilter_nump(self,nb):
        for i in range(nb):
            img_temp = self.array.copy()
            for x in range(1,self.width-1):
                for y in range(1,self.height-1):
                    sum = np.sum(self.array[y-1:y+2,x-1:x+2])
                    if sum < 1100 :
                        img_temp[y,x] = 0
                    else:
                        img_temp[y,x] = 255
            self.array = img_temp
        return self

    def addRectangle(self, x, y, w, h, color):
        cv2.rectangle(self.array, (x, y), (x + w, y + h), color, 2)
        return self

    def addLine(self, x1, y1, x2, y2, color):
        cv2.line(self.array, (x1, y1), (x2, y2), color, 2)
        return self

    def copy(self):
        img_temp = Image(self.path)
        img_temp.array = self.array.copy()
        img_temp.width = self.width
        img_temp.height = self.height
        img_temp.nom = self.nom
        return img_temp

    def show(self, name):
        cv2.imshow(name, self.array)
