import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.cluster import KMeans

def main():
	params = getparams()
	img_path = params['img_path']
	img_size = params['img_size']
	n_colors = params['n_colors']

	img_array = getimage(img_path, img_size)

	rotated = False
	if img_array.shape[0] > img_array.shape[1]:
		img_array = np.rot90(img_array, k=3)
		rotated = True

	k_colors = getcolors(img_array.reshape((-1, 3)), n_colors)

	img_height, img_width, _ = img_array.shape
	bar_height = img_height * 0.2
	bar_width = img_width / n_colors
	bar_coord = np.arange(0, img_width, bar_width)

	plt.bar(
		bar_coord,
		bottom = img_height + bar_height * 0.2,
		height = bar_height,
		width = bar_width,
		color = k_colors,
		align = 'edge'
	)
	plt.axis([0, img_width, img_height + bar_height * 1.2, 0])

	plt.imshow(img_array)
	plt.axis('off')
	plt.show()


def getparams():
	if len(sys.argv) > 1 and os.path.isfile(sys.argv[1]):
		img_path = sys.argv[1]
		print(f"Using provided image {img_path}")
	else:
		img_path = 'images/palette-demo1.jpg'
		print(f"Using DEFAULT image {img_path}")

	print('Provide the following parameters, or press ENTER to use DEFAULTS...')

	img_size = input('  Limit image size on either axis to (default, keep original)\t: ')
	img_size = False if not img_size else int(img_size)

	n_colors = input('  Number of colors to generate in palette (default, 6 colors)\t: ')
	n_colors = 6 if not n_colors else int(n_colors)

	return {
		'img_path': img_path,
		'img_size': img_size,
		'n_colors': n_colors,
	}


def getimage(path, size):
	with Image.open(path) as img:
		if size:
			img.thumbnail((size, size))
		img = img.convert('RGB')
		img_array = np.array(img)
	return img_array


def getcolors(img, n):
	k_colors = KMeans(n_clusters=n).fit(img).cluster_centers_
	return np.sort(k_colors/256, 0)


if __name__ == '__main__':
	main()