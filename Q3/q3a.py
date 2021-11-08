import pywt
import os
import cv2
import numpy as np

root = os.getcwd()
img_dir = os.path.join(root, "../images")
lena_path = os.path.join(img_dir, "lena.bmp")
lena = cv2.imread(lena_path, 0)

LL, (LH, HL, HH) = pywt.dwt2(lena, 'haar')
#LL = (255*(LL-np.min(LL)))/(np.max(LL)-np.min(LL))
#LH = (255*(LH-np.min(LH)))/(np.max(LH)-np.min(LH))
#HL = (255*(HL-np.min(HL)))/(np.max(HL)-np.min(HL))
#HH = (255*(HH-np.min(HH)))/(np.max(HH)-np.min(HH))
fr = np.hstack((LL, LH))
sr = np.hstack((HL, HH))
full = np.vstack((fr, sr))

cv2.imwrite(os.path.join(img_dir, "3A/full.png"), full)




