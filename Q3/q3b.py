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
LH = (255*(LH-np.min(LH)))/(np.max(LH)-np.min(LH))
HL = (255*(HL-np.min(HL)))/(np.max(HL)-np.min(HL))
HH = (255*(HH-np.min(HH)))/(np.max(HH)-np.min(HH))
plt.hist(LL.flatten(), bins=255, range=[0, 255])
plt.title("LL")
plt.savefig(os.path.join(img_dir, "3B/ll.png"))
plt.hist(LH.flatten(), bins=255, range=[0, 255])
plt.title("LH")
plt.savefig(os.path.join(img_dir, "3B/lh.png"))
plt.hist(HL.flatten(), bins=255, range=[0, 255])
plt.title("HL")
plt.savefig(os.path.join(img_dir, "3B/hl.png"))
plt.hist(HH.flatten(), bins=255, range=[0, 255])
plt.title("HH")
plt.savefig(os.path.join(img_dir, "3B/hh.png"))
