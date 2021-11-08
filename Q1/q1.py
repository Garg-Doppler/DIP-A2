import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

root = os.getcwd()
img_dir = os.path.join(root, "../images")
lena_path = os.path.join(img_dir, "lena.bmp")

lena = cv2.imread(lena_path, 0)

L1 = np.array([[0, -1, 0],
               [-1, 4, -1],
               [0, -1, 0]])

L2 = np.array([[-1, -1, -1],
               [-1, 8, -1],
               [-1, -1, -1]])

sx = np.array([[-1, -2, -1], 
               [0, 0, 0], 
               [1, 2, 1]])

sy = np.array([[-1, 0, 1], 
               [-2, 0, 2], 
               [-1, 0, 1]])

freqlena = np.log(np.abs(np.fft.fft2(lena)))

filter_name = ['Laplacian-1D', 'Laplacian-2D', 'Sobel-X', 'Sobel-Y']
filters = [L1, L2, sx, sy]
filtered = [cv2.filter2D(src=lena, ddepth=-1, kernel=x) for x in filters]
fft_filtered = [np.fft.fft2(x) for x in filtered]

freq_filter = [np.divide(z, freqlena) for z in fft_filtered]

for i in range(4):
    print(np.abs(freq_filter[i]))
    plt.imshow(np.log(np.abs(freq_filter[i])), cmap='gray')
    plt.title("Transfer Function of {}".format(filter_name[i]))
    plt.show()



