from PIL import Image, ImageDraw

width = 1024
height = 1023
r = 3
etoiles = []

filename = "output/m13-red-0.fits.dat"
fichier = open(filename, "r")
lignes = fichier.readlines()

for ligne in lignes :
    if ligne[0] == "#":
        continue

    colonnes = ligne.split()

    x = colonnes[4]
    y = colonnes[5]
    magn = colonnes[2]

    etoile = [x, y, magn]
    etoiles.append(etoile)

etoiles = sorted(etoiles, key = lambda etoile: etoile[2])
etoiles.reverse()


image = Image.open("output/5.png")
draw = ImageDraw.Draw(image)

for etoile in etoiles[0:5] :

    x = float(etoile[0])
    #y = float(etoile[1])
    y = height - float(etoile[1])

    draw.ellipse([x-r,y-r,x+r,y+r], outline="red")
    #draw.text( [x, y+r+3] , str(i) )

del draw
image.save("output/5-circles.png")

print(etoiles[0:5])
