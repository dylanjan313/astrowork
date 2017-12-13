# -*- coding: utf8

import numpy as np
from math import sqrt

filters = ["red","blue","green","green2"]

# STEP 1: Create a big multi-dim array
# to store stars data (x,y,magn) for each image in each filter

stars = []
# stars[f][j][i]
#   f: filter id
#   j: image nb
#   i: star id
#       [0]: x
#       [1]: y
#       [2]: magn

for filter_id in range(0,4) :
    filter_name = filters[filter_id]
    stars_current_filter = []

    for j in range(0,16) :
        stars_current_image = []

        filename = "output/m13-"+filter_name+"-"+ str(j) + ".fits.dat"
        f = open(filename, "r")

        lines = f.readlines()

        for line in lines :

            # Header: continue
            if line[0] == "#":
                continue

            columns = line.split()

            star = []
            star.append(float(columns[4]))
            star.append(float(columns[5]))
            star.append(float(columns[2]))

            stars_current_image.append(star)

        f.close()

        stars_current_filter.append(stars_current_image)

    stars.append(stars_current_filter)

# STEP 2 : Find, for a given image, the matching magnitudes
# in all filters and write the result in a file
# with those columns: x y magn_red magn_blue magn_green magn_green2

#for j in range(0 ,1) :
for j in range(0 ,16) :
    rows = []

    fw = open("output/stars-"+str(j)+".txt","w")
    fw.write("# x y magn_red magn_blue magn_green magn_green2 \n")

    for i in range(0, len(stars[0][j])) :
    #for i in range(0, 100) :

        star_red = stars[0][j][i]

        row = []
        x = star_red[0]
        y = star_red[1]
        magn_red = star[2]

        print("////////////////////////")
        print("Image : " + str(j))
        print("Star : " + str(i))
        print("x = " + str(x))
        print("y = " + str(y))
        print("magn_red = " + str(magn_red))
        print("")

        row.append(str(x))
        row.append(str(y))
        row.append(str(magn_red))

        for f in range(1,4) :
            # stars_set: the set to find the nearest star from
            stars_set = stars[f][j]

            distances = []

            for k in range(0, len(stars_set)) :
                star = stars_set[k]

                x_t = star[0]
                y_t = star[1]
                magn_t = star[2]

                distance = sqrt( (x - x_t)**2 + (y - y_t)**2 )

                distances.append([k,distance])

            distances = sorted(distances, key = lambda x: x[1])

            nearest_star_id = distances[0][0]
            nearest_star = stars_set[nearest_star_id]
            row.append(str(nearest_star[2]))

            print("---------------")
            print("For filter " + filters[f] + ", the nearest star is :")
            print("x = " + str(nearest_star[0]) )
            print("y = " + str(nearest_star[1]) )
            print("magn = " + str(nearest_star[2]) )

        rows.append(row)

    for row in rows :
        fw.write(" ".join(row) + "\n")

    fw.close()
