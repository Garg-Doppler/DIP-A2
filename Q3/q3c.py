import pywt
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

root = os.getcwd()
img_dir = os.path.join(root, "../images")
lena_path = os.path.join(img_dir, "lena.bmp")
lena = cv2.imread(lena_path, 0)

LL, (LH, HL, HH) = pywt.dwt2(lena, 'haar')
LL = (255*(LL-np.min(LL)))/(np.max(LL)-np.min(LL))
imgq = LL.astype('int')
print(np.max(imgq), np.min(imgq))

lst = []
for i in imgq.flatten():
    lst.append(np.binary_repr(i ,width=8))

planes = [np.multiply(2**(7-i), np.array([int(bit[i]) for bit in lst],dtype = np.uint8).reshape(imgq.shape[0],imgq.shape[1])) for i in range(8)]

def rmse(a, b):
    rmse = np.sqrt(np.mean(np.square(a-b)))
    return rmse.astype(np.float64)

for m in range(1, 8):
    quantI = planes[7]
    for i in range(1, m):
        quantI += planes[7-i]
    
    plt.hist(quantI.flatten(), bins=255, range=[0, 255])
    plt.title("{}-bit histogram".format(m))
    plt.savefig(os.path.join(img_dir, "3C/{}bit_hist.png".format(m)))

    recon_img = pywt.idwt2((quantI.astype(np.double), (LH, HL, HH)), 'haar')
    print("\nM={}:\n".format(m))
    print("The RMSE between the reconstructed and original image is: {}".format(rmse(lena, recon_img)))
    print("The Compression Ratio for m={0} is {1}".format(m, 8.0/m))
    cv2.imwrite(os.path.join(img_dir, "3C/{}bit_reconstructed.png".format(m)), recon_img)
    cv2.imwrite(os.path.join(img_dir, "3C/{}bit.png".format(m)), quantI)





