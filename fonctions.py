from astropy.io import fits
import os

def touch(path):
    with open(path, 'a'):
        os.utime(path, None)

def read_matrix(path):
    image = fits.open(path)
    matrix = image[0].data
    image.close()

    return matrix

def write_matrix(path, matrix):

    if not os.path.isfile(path):
        touch(path)

    hdu = fits.PrimaryHDU(matrix)
    hdulist = fits.HDUList([hdu])
    hdulist.writeto(path)
