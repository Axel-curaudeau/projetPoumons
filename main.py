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


def is_inside(x, y):
    """
    Check if a point is inside the echographie

    Parameters
    ----------
    x : int
        x coordinate of the point
    y : int
        y coordinate of the point

    Returns
    -------
    bool
        True if the point is inside the echographie shape, False otherwise
    """
    if (B_Y - A_Y) / (B_X - A_X) * x + A_Y >= y:
        return False
    if (D_Y - C_Y) / (D_X - C_X) * x + C_Y <= y:
        return False
    if -0.00239 * y * y + 1.62919 * y - 235 >= x:
        return False
    if -0.00091 * y * y + 0.61765 * y + 300 <= x:
        return False
    return True


def proba(img, color_step):
    proba_value = [0 for _ in range(0, 254, color_step)]
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            if is_inside(x, y):
                proba_value[int(img[x, y][0] / color_step)] += 1
    for x in range(len(proba_value)):
        proba_value[x] = proba_value[x] / (img.shape[0] * img.shape[1])
    return proba_value


def entropia(img, color_step):
    entropia_value = 0
    proba_value = proba(img, color_step)
    for value in range(len(proba_value)):
        if proba_value[value] != 0:
            entropia_value += proba_value[value] \
                              * np.log(1 / proba_value[value])
    return entropia_value


def cut_image(img, nb_cut):
    image_list = []
    x = 0
    y = 0
    cutted_image_width = int(img.shape[0] / nb_cut)
    cutted_image_height = int(img.shape[1] / nb_cut)
    # print(cutted_image_height, cutted_image_width)
    for i in range(1, nb_cut + 1):
        for j in range(1, nb_cut + 1):
            print(x, (i * cutted_image_width), y, (j * cutted_image_height))
            image_list.append(img[x: (i * cutted_image_width),
                                  y: (j * cutted_image_height)])

            y = j * cutted_image_height
        x = i * cutted_image_width
        y = 0
    return image_list


image = cv2.imread(ressources_path + "2019010A.jpg")

for i in range(0, image.shape[0]):
    for j in range(0, image.shape[1]):
        if not is_inside(i, j):
            image[i, j] = [100, 0, 0]

print(entropia(image, 1))

imagette = cut_image(image, 4)

# cv2.imshow("wow", image)
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
