from fonctions import read_matrix, write_matrix
import config

def reduction(number, filter) :

    # On charge le DARK et le FLAT associé au filtre choisi
    dark = read_matrix("output/master-dark-"+filter+".fits")
    flat = read_matrix("output/master-flat-"+filter+".fits")

    LIST = None

    # On attribue à LIST la liste des images de M13_BLUE
    # dans le filtre considéré
    if filter == "blue":
        LIST = config.M13_BLUE
    elif filter == "red":
        LIST = config.M13_RED
    elif filter == "green":
        LIST = config.M13_GREEN
    elif filter == "green2":
        LIST = config.M13_GREEN2
    else:
        print("Invalid filter")
        return 0

    # On charge la matrice de l'image demandé
    image = read_matrix(LIST[number])

    # Petit calcul puis sauvegarde
    image_finale = (image - dark) / (flat - dark)
    write_matrix("output/m13-"+filter+"-"+str(number)+".fits", image_finale)

# On applique la fonction sur les 16 images dans les 4 filtres
# Les images réduites auront des numéros de 0 à 15
# au lieu de 5 à 20 pour plus de facilité ultérieurement
# puisque nous travaillerons avec les images réduites
for i in range(0,16) :
    reduction(i, "blue")
    reduction(i, "red")
    reduction(i, "green")
    reduction(i, "green2")
