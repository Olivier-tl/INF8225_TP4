###################################################
##	sobel.py : utility script for applying a sobel filter to all images in a folder
##	@author Luc Courbariaux 2018
###################################################

import argparse

parser = argparse.ArgumentParser(description='gets all images in INPUT folder, applies a sobel filter them and puts them in OUTPUT directory.')
parser.add_argument('-i', '--input', nargs='?', default="./", help='folder from which the images')
parser.add_argument('-o', '--output', nargs='?', default="./dataset/", help='folder to store the images')
args = parser.parse_args()



import os
import numpy
from PIL import Image
import scipy
from scipy import ndimage

input = args.input
output = args.output

try:
	os.mkdir(output)
except:
	pass


for file in os.listdir(input):
	#sobel filter
	#based on https://stackoverflow.com/questions/7185655
	if file.endswith(".jpg") or file.endswith(".bmp") :
		im = scipy.misc.imread(input + "/" + file)
		im = im.astype('int32')
		dx = ndimage.sobel(im, 0)  # horizontal derivative
		dy = ndimage.sobel(im, 1)  # vertical derivative
		mag = numpy.hypot(dx, dy)  # magnitude
		mag *= 255.0 / numpy.max(mag)  # normalize (Q&D)
		mag = mag.mean(axis=2)
		mag = mag.astype("uint8")
		img = Image.fromarray(mag)
		img.save(output + "/" + file)