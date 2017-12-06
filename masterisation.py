from fonctions import read_matrix, write_matrix
import config

import numpy as np


def masterize(input_files, output):

    images = []

    for filename in input_files :
        matrix = read_matrix(filename)
        images.append(matrix)

    median = np.median(images, axis=0)

    write_matrix(output, median)


masterize(config.DARKS_BLUE,   'output/master-dark-blue.fits')
masterize(config.DARKS_RED,    'output/master-dark-red.fits')
masterize(config.DARKS_GREEN,  'output/master-dark-green.fits')
masterize(config.DARKS_GREEN2, 'output/master-dark-green2.fits')

masterize(config.FLATS_BLUE,   'output/master-flat-blue.fits')
masterize(config.FLATS_RED,    'output/master-flat-red.fits')
masterize(config.FLATS_GREEN,  'output/master-flat-green.fits')
masterize(config.FLATS_GREEN2, 'output/master-flat-green2.fits')
