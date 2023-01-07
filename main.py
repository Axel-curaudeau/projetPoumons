import Patient
import Tools
import graph

'''
Affihche le graphe des valeurs d'entropies des images (jpg) en fonction du nombre de lignes B présente sur cette image.
Le nombre de ligne B a été récuperé dans le fichier Excel fourni avec les images.
Il nous donne le nombre de ligne B de chaque image.'''
# graph.graph_entropy_all_image("ressources/Patients/PatientsList2.txt")
# graph.graph_entropy_all_image("ressources/Patients/PatientsList3.txt")

'''Calcule l'entropie avec la fonction sub_image. Cette fonction (sub_image) cherche une sous-image dans l'image 
d'origine afin d'éviter les ombres causées par les côtes, et ainsi obtenir une entropie plus précise. Elle affiche le 
graphe des valeurs d'entropies des images (jpg) en fonction du nombre de lignes B présente sur cette image.'''
# graph.graph_sub_image("ressources/Patients/PatientsList2.txt")

'''Calcule l'entropie avec la fonction slide_entropy. Cette fonction (slide_entropy) calcule l'entropie d'un 
rectangle horizontal ou vertical de l'image, et fait glisser ce rectangle jusqu'à la fin de l'image. Elle affiche le 
graphe de l'évolution de l'entropie en fonction de la position du rectangle.'''
graph.graph_sub_image_slide_entropy("./ressources/Patients/01Patient 1CP01/101M0/2019010A.jpg")

'''
'''
# Tools.compute_entropy_all_dicom_file()

'''
Tests
'''
folder_path = "C:/Users/axell/OneDrive - Université de Tours/Boucles echo TOUPIE (2)"
patient_object_list = Patient.search_all_patient(folder_path)
Tools.print_patients(patient_object_list)

dicom_image = patient_object_list[4].list_of_exams[0].dicom_image_list[0].image_array()


'''
for image in dicom_image:
    sub_image = EchoTools.sub_image(image)
    print(sub_image)
    cv2.imshow("image", sub_image)
    cv2.imshow("image2", image)
    cv2.waitKey(0)
'''
