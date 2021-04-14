import primes
import math
import numpy as np
from PIL import Image

def run(params, v=False):
	txt_path = params['txt_path']
	end_with = params['end_with']
	img_path = params['img_path']
	exp_path = params['exp_path']

	if v: print(f"Opening text file: {txt_path}...")
	txt_string = gettext(txt_path, endwith=end_with)

	prime_pixels = primes.getpixels(len(txt_string), v)
	min_pixels = prime_pixels[-1]

	if v: print(f"Opening image file: {img_path}...")
	img_array = getimage(img_path, minpixels=min_pixels)

	if v: print("Ready: Embeding text into image...")
	img_array = encode(img_array, prime_pixels, txt_string)
	
	if v: print(f"DONE: Saving image as {exp_path}...")
	saveimage(img_array, exp_path)


def gettext(path, endwith=False):
	def markend(text, endwith):
		return text + endwith if endwith not in text else False
	
	with open(path, 'r') as file:
		text = file.read()
	if endwith:
		text = markend(text, endwith)
	return text


def getimage(path, minpixels=False):
	def newdimension(oldsize, minpixels):
		old_W, old_H = oldsize
		ratio = old_W / old_H
		x = math.sqrt(minpixels / ratio)    #Because, minpixels = ratio*x * x
		new_W = math.ceil(ratio * x)
		new_H = math.ceil(x)
		return new_W, new_H

	with Image.open(path) as img:
		img = img.convert('L')
		if minpixels:
			img = img.resize(newdimension(img.size, minpixels))
		image = np.array(img)
	return image


def encode(image, pixels, text):
	columns = image.shape[1]
	for pixel, char in zip(pixels, text):
		r = pixel // columns
		c = pixel % columns
		image[r,c] = ord(char)
	image = image.astype(np.uint8)
	return image


def saveimage(image, path):
	img = Image.fromarray(image)
	img.save(path, format='PNG', optimize=False)


if __name__ == '__main__':
	params = {
		'txt_path': 'files/usa-constitution.txt',
		'end_with': '1787',
		'img_path': 'images/lincoln-cracked.png',
		'exp_path': 'exports/lincoln-encoded.png'
	}
	run(params, v=True)