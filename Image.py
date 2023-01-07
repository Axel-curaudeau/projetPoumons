class Image:
    name = ""
    path = ""
    array = None

    def __init__(self, img_name, img_path):
        self.path = img_path
        # self.array = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        self.name = img_name
