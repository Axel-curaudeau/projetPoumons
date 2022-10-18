import cv2

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


def isInside(i, j):
    if (B_Y - A_Y)/(B_X - A_X) * i + A_Y >= j:
        return False
    if (D_Y - C_Y)/(D_X - C_X) * i + C_Y <= j:
        return False
    if -0.00239*j*j + 1.62919*j - 235 >= i:
        return False
    if -0.00091*j*j + 0.61765*j + 300 <= i:
        return False
    return True


image = cv2.imread(ressources_path + "2019010A.jpg")

for i in range(0, image.shape[0]):
    for j in range(0, image.shape[1]):
        if isInside(i, j) == False:
            image[i, j] = [100, 0, 0]

cv2.imshow("wow", image)
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
