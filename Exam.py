import os
import Image
import DicomImage


class Exam:

    path = ""
    name = ""
    image_list = []
    dicom_image_list = []

    def __init__(self, exam_name, exam_path):
        self.name = exam_name
        self.path = exam_path
        self.image_list = []
        self.dicom_image_list = []
        dir_list = os.listdir(exam_path)
        for file in dir_list:
            if os.path.isdir(self.path + "/" + file):
                self.name += "/" + file
                dir_sublist = os.listdir(self.path + "/" + file)
                for subfile in dir_sublist:
                    if not subfile.__contains__("."):
                        self.dicom_image_list.append(DicomImage.DicomImage(self.path + "/" + file + "/" + subfile, subfile))
                    else:
                        self.image_list.append(Image.Image(subfile, self.path + "/" + file + "/" + subfile))
            elif not file.__contains__("."):
                self.dicom_image_list.append(DicomImage.DicomImage(self.path + "/" + file, file))
            elif file.__contains__(".ini"):
                pass
            else :
                self.image_list.append(Image.Image(file, self.path + "/" + file))
            # print(self.name)

