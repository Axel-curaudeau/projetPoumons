import cv2

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

    def __init__(self, imgPath):
        self.path = imgPath
        self.array = cv2.imread(imgPath)
        self.nom = imgPath.split("/")[-1].split(".")[0]
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
            for j in range(0, self.width,):
                img_temp[i, j] = [0, 0, 255]
        for i in range(0, self.width, step):
            for j in range(0, self.height):
                img_temp[j, i] = [0, 0, 255]
        cv2.imshow("grid", img_temp)

    def filter(self, level):
        echo_temp = self.copy()
        for i in range(0, self.height):
            for j in range(0, self.width):
                if echo_temp.array[i, j][0] < level:
                    echo_temp.array[i, j] = [0, 0, 0]
                else:
                    echo_temp.array[i, j] = [255, 255, 255]
        return echo_temp

    def addRectangle(self, x, y, w, h, color):
        cv2.rectangle(self.array, (x, y), (x + w, y + h), color, 2)
        return self

    def addLine(self, x1, y1, x2, y2, color):
        cv2.line(self.array, (x1, y1), (x2, y2), color, 2)
        return self

    def copy(self):
        return Image(self.path)

    def show(self, name):
        cv2.imshow(name, self.array)
