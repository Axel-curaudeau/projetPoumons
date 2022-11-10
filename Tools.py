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
