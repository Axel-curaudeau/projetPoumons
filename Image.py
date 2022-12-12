import cv2


class Image:
    name = ""
    path = ""
    array = None

    def __init__(self, img_name, img_path):
        self.path = img_path
        # self.array = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        self.name = img_name



'''
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
'''

