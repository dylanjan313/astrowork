from fonctions import read_matrix, write_matrix
import config

def reduction(number, filter) :

    dark = read_matrix("output/master-dark-"+filter+".fits")
    flat = read_matrix("output/master-flat-"+filter+".fits")

    LIST = None

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

    image = read_matrix(LIST[number])

    image_finale = (image - dark) / (flat - dark)

    write_matrix("output/m13-"+filter+"-"+str(number)+".fits", image_finale)

for i in range(0,16) :
    reduction(i, "blue")
    reduction(i, "red")
    reduction(i, "green")
    reduction(i, "green2")
