# -*- coding: utf8

# CODE POUR LE FILTRE ROUGE
# Les chemins doivent être adaptés pour les autres filtres

import numpy as np
from math import sqrt

# Créer une matrice images[j][i][0] = coord x
#                   images[j][i][1] = coord y
#                   images[j][i][2] = magnitude
#
#       j = numéro de l'image (de 0 à 15)
#       i = numéro de l'object dans l'image j


eps = 5         # Notre "petit" epsilon
images = []     # Notre tableau

# Parsing des fichiers .dat dans le filtre rouge
for j in range(0,16) :
    filename = "output/m13-red-"+ str(j) + ".fits.dat"

    image = []

    fichier = open(filename, "r")
    lignes = fichier.readlines()

    # "lignes" est un tableau de chaines
    i=0
    for ligne in lignes:

        # Si le 1er caractère de la ligne est le dièse,
        # on passe à la ligne suivante
        # continue: passe le reste de la boucle et reprend à l'itération suivante
        if ligne[0] == "#":
            continue

        # Séparer la chaine "ligne" en un tableau
        # Séparateur : tout espace blanc (tabul, espace, plrs espaces, ...)
        colonnes = ligne.split()

        # Les indices sont déterminés par le format de sortie de sextractor
        # Modifiable via le fichier de configuration
        etoile = []
        etoile.append(float(colonnes[4]))
        etoile.append(float(colonnes[5]))
        etoile.append(float(colonnes[2]))

        image.append(etoile)

        i += 1


    fichier.close()
    images.append(image)

fichier = open("output/avg-magnitudes-red.txt","w")
fichier.write("# x y avg_magn \n")

# Boucle sur toutes les étoiles k détectées dans la 1ère image
for k in range(0, len(images[0])):

    # Liste des magnitudes trouvées pour l'étoile k
    magnitudes = []
    magnitudes.append(images[0][k][2]) # La 1ère magn est celle provenant de 5.fits

    # Pour chaque étoile k de la première image
    # Identifier l'étoile (une seule) la plus proche dans tous les fichiers j.fits
    # j variant de 6 à 20 (inclus)

    # Pour chaque étoile détectée par sextractor dans le fichier 5.fits
    # On récupère les coordonnées
    x = images[0][k][0]
    y = images[0][k][1]

    print("=======================================================")
    print("Star k=" + str(k) + " in 1st image over " + str(len(images[0])) )

    # Pour chaque image (de 1 à 15)
    for j in range(1,16) :

        distances = []

        # Pour chaque étoile i détectée dans "j.fits"
        for i in range(0,len(images[j])) :

            # On récupère les coords de l'étoile i détectée dans "j.fits"
            x_test = images[j][i][0]
            y_test = images[j][i][1]

            # On calcule la distance en pixels par rapport à l'étoile k dans 5.fits
            dist = sqrt( (x - x_test)**2 + (y - y_test)**2 )

            distances.append((i,dist))

        distances = sorted(distances, key = lambda x: x[1])

        # Identification de l'indice i de l'étoile la plus proche dans l'image j
        min_i    = distances[0][0]

        # On peut ajouter sa magnitude dans la liste
        magnitudes.append(images[j][min_i][2])


    # Une fois que la liste des magnitudes est remplie, on peut calculer la moyenne
    print("Average magnitude: " + str(np.mean(magnitudes)) )
    fichier.write(str(x) + " " + str(y) + " " + str(np.mean(magnitudes)) + "\n")

fichier.close()
print("FINAL END")
