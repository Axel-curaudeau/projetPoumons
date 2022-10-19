import cv2
import numpy as np

ressources_path = "ressources/"

STEP = 20

CUT_NB = 3

A_X = 0.0
A_Y = 208.0
B_X = 298.0
B_Y = 0.0

C_X = 0.0
C_Y = 473.0
D_X = 300.0
D_Y = 680.0


def isInside(x, y):
    if (B_Y - A_Y)/(B_X - A_X) * x + A_Y >= y:
        return False
    if (D_Y - C_Y)/(D_X - C_X) * x + C_Y <= y:
        return False
    if -0.00239*y*y + 1.62919*y - 235 >= x:
        return False
    if -0.00091*y*y + 0.61765*y + 300 <= x:
        return False
    return True


def proba(img, colorStep):
    probaValue = [0 for _ in range(0, 254, colorStep)]
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            if isInside(x, y):
                probaValue[int(img[x, y][0]/colorStep)] += 1
    for x in range(len(probaValue)):
        probaValue[x] = probaValue[x]/(img.shape[0] * img.shape[1])
    return probaValue


def entropia(img, colorStep):
    entropiaValue = 0
    probaValue = proba(img, colorStep)
    for v in range(len(probaValue)):
        if probaValue[v] != 0:
            entropiaValue += probaValue[v] * np.log(1/probaValue[v])
    return entropiaValue


def imgCut(img, nbCut):
    listImage = []
    x, y = 0, 0
    cutImageSizeX = int(img.shape[0]/nbCut)
    cutImageSizeY = int(img.shape[1]/nbCut)
    #print(cutImageSizeY, cutImageSizeX)
    for i in range(1, nbCut + 1):
        for j in range(1, nbCut + 1):
            print(x, (i * cutImageSizeX), y, (j * cutImageSizeY))
            listImage.append(img[x: (i * cutImageSizeX), y:(j * cutImageSizeY)])

            y = j * cutImageSizeY
        x = i * cutImageSizeX
        y = 0
    return listImage




image = cv2.imread(ressources_path + "2019010A.jpg")

for i in range(0, image.shape[0]):
    for j in range(0, image.shape[1]):
        if isInside(i, j) == False:
            image[i, j] = [100, 0, 0]

print(entropia(image, 1))

imagette = imgCut(image, 4)

#cv2.imshow("wow", image)
for i in range(len(imagette)):
    cv2.imshow(str(i), imagette[i])
cv2.waitKey(0)

"""
#define STEP 20

#define CUT_NB 3

#define A_X 0
#define A_Y 208
#define B_X 300
#define B_Y 0

#define C_X 0
#define C_Y 473
#define D_X 300
#define D_Y 680

/////////////////  Images  //////////////////////

void addLimits(Mat img, Vec3b color, int i, int j) {
    if ((float)((float)(B_Y - A_Y)/(float)(B_X - A_X)) * i + A_Y >= j) {
        color[0] = color[1] = 0;
        color[2] = 100;
        img.at<Vec3b>(i, j) = color;
        //cout << "i: " << i << " j: " << j << endl;
    } else if ((float)((float)(D_Y - C_Y)/(float)(D_X - C_X)) * i + C_Y <= j) {
        color[0] = color[1] = 0;
        color[2] = 100;
        img.at<Vec3b>(i, j) = color;
    } else if (-0.00239*j*j + 1.62919*j - 235 >= i) {
        color[0] = color[1] = 0;
        color[2] = 100;
        img.at<Vec3b>(i, j) = color;
    } else if (-0.00091*j*j + 0.61765*j + 300 <= i) {
        color[0] = color[1] = 0;
        color[2] = 100;
        img.at<Vec3b>(i, j) = color;
    }
}

bool isInside(int i, int j) {
    if ((float)((float)(B_Y - A_Y)/(float)(B_X - A_X)) * i + A_Y >= j) {
        return false;
    } else if ((float)((float)(D_Y - C_Y)/(float)(D_X - C_X)) * i + C_Y <= j) {
        return false;
    } else if (-0.00239*j*j + 1.62919*j - 235 >= i) {
        return false;
    } else if (-0.00091*j*j + 0.61765*j + 300 <= i) {
        return false;
    }
    return true;
}


int main() {
    string path = "/Users/thomasraymond/Desktop/2019010A.jpg";
    Mat img = imread(path);
    for (int i = 0; i < img.rows; i++) {
        for (int j = 0; j < img.cols; j++) {
            Vec3b color = img.at<Vec3b>(i, j);
            addLimits(img, color, i, j);
        }
    }

    imshow("Image", img);
    waitKey(0);
    return 0;
}
"""
