import cv2

from Analyzer import Analyzer

RESSOURCES_PATH = "ressources/"

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

def entropy_test():
    fichier = open("entropyList-1.txt", "w")
    for i in range(322):
        image = cv2.imread(RESSOURCES_PATH + "poumons2/" + str(i) + ".jpg")
        analyze = Analyzer(image)
        fichier.write(str(analyze.entropy(1)) + "\n")
        print(i)

# --------- Main ---------

image = cv2.imread(RESSOURCES_PATH + "2019010A.jpg")


ImageAnalyzer = Analyzer(image)


for i in range(0, image.shape[0]):
    for j in range(0, image.shape[1]):
        if not ImageAnalyzer.is_inside(i, j):
            image[i, j] = [100, 0, 0]


print(ImageAnalyzer.entropy(10))

#entropy_test()

'''
imagette = cut_image(image, 2)

# cv2.imshow("wow", image)
for i in range(len(imagette)):
    cv2.imshow(str(i), imagette[i])
cv2.waitKey(0)'''