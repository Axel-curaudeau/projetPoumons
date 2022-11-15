import csv

RESSOURCES_PATH = "ressources/"


def generate_patient_list_txt_file():
    file = open(RESSOURCES_PATH + "Patients/BaseAnnoteeWorkBookModif.csv")
    csv_reader = csv.reader(file)
    lines = []

    for row in csv_reader:
        lines.append(row)
    file.close()
    result = []
    for i in range(len(lines)):
        sub_line = []
        for j in range(len(lines[i])):
            temp = lines[i][j].split(";")
            for k in temp:
                if len(k) != 0:
                    sub_line.append(k)
        result.append(sub_line)
    result.pop(0)
    file = open(RESSOURCES_PATH + "Patients/PatientsList.txt", "w")
    for i in result:
        for j in i:
            file.write(j)
            file.write(";")
        file.write("\n")
    file.close()


def read_patient_list_file(patient_file_path):
    patient_file = open(patient_file_path, "r")
    patient_list = patient_file.readlines()
    patient_file.close()
    result = []
    for line in patient_list:
        result.append(line.split(";"))
        result[-1].pop(-1)
    return result


def write_patient_list_file(patient_file_path, patient_list):
    patient_file = open(patient_file_path + "2", "w")
    for i in patient_list:
        for j in i:
            patient_file.write(str(j))
            patient_file.write(";")
        patient_file.write("\n")
    patient_file.close()


def get_echo_path(patient):
    num_patient = patient[0][len(patient[0]) - 2:]
    path = ""
    if int(num_patient) <= 8:
        path = "0"
    path += patient[0] + "/"
    if int(num_patient) <= 10:
        path += "1"
    else:
        path += "10"
    path += num_patient + patient[1] + "/" + patient[2] + ".jpg"
    return path