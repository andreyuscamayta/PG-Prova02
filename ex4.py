import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def transposta(m):
	width = len(m[0])
	height = len(m)
	resposta=[[0 for x in range(width)] for y in range(height)]	
	for i in range(height):
		for j in range(width):
			resposta[i][j] = m[i][j]
	return np.array(resposta)

img = cv.imread('resources/unifafibe.jpg')
b,g,r = cv.split(img)
b1 = transposta(b)
g1 = transposta(g)
r1 = transposta(r)
img2 = cv.merge((b1,g1,r1))
plt.subplot(121),plt.imshow(img, cmap="gray"),plt.title('Original')
plt.subplot(122),plt.imshow(img2, cmap="gray"),plt.title('Processed')
plt.show()