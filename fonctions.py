from astropy.io import fits
import os

def touch(path):
    with open(path, 'a'):
        os.utime(path, None)

def read_matrix(path):
    # Cette fonction ouvre le fichier FITS et
    # retourne la matrice bi-dim
    image = fits.open(path)
    matrix = image[0].data
    image.close()

    return matrix


def write_matrix(path, matrix):
    # Cette fonction crée une nouvelle image FITS

    if not os.path.isfile(path):
        # Pour éviter une erreur, le fichier doit exister
        touch(path)

    # Méthode proposée dans la doc pour générer l'image
    hdu = fits.PrimaryHDU(matrix)
    hdulist = fits.HDUList([hdu])
    hdulist.writeto(path)
