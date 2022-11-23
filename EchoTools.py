import cv2

import Entropy


def smooth(image, filter, kernel_size):
    image_filter = cv2.threshold(image, filter, 255, cv2.THRESH_BINARY)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    image_open = cv2.morphologyEx(image_filter, cv2.MORPH_OPEN, kernel)
    image_open_close = cv2.morphologyEx(image_open, cv2.MORPH_CLOSE, kernel)
    return image_open_close

def sub_image(image):
    intersection = []
    image_filtered = smooth(image, 30, 7)
    width = len(image_filtered[0])
    height = len(image_filtered)

    for i in range(50, width - 50):
        if image_filtered[300, i] == 255 and image_filtered[300, i - 1] == 0:
            intersection.append((i, i + 1, "NB"))
        elif image_filtered[300, i] == 0 and image_filtered[300, i - 1] == 255:
            intersection.append((i, i + 1, "BN"))

    for i in intersection:
        cv2.line(image_filtered, (i[0], 298), (i[0] + 10, 298), 160, 2)
        # image_filtered.addLine(i[0], 298, i[0] + 1, 298, (0, 0, 255))

    for i in range(1, len(intersection)):
        if intersection[i][2] == "BN" and intersection[i - 1][2] == "NB":
            xl = intersection[i - 1][0]
            xr = intersection[i][0]

    # cv2.rectangle(image, (xl, 300), (xr, 200), 155, 2)
    # image.addRectangle(xl, 300, xr - xl, -100, (0, 0, 255))

    #cv2.imshow("filter", image_filtered)
    #print(xl, " ", xr)
    return image[200:300, xl:xr]

def slide_entropy(img, slide_width, orientation):
    list_entropy = []
    if orientation == "vertical":
        for x in range(0, img.shape[1] - slide_width):
            list_entropy.append(Entropy.compute_entropy(img[:, x:x + slide_width]))
    elif orientation == "horizontal":
        for y in range(0, img.shape[0] - slide_width):
            list_entropy.append(Entropy.compute_entropy(img[y:y + slide_width, :]))
    return list_entropy