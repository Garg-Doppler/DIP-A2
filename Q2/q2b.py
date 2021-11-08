import os
import numpy as np
import matplotlib.pyplot as plt
import cv2

root = os.getcwd()
img_dir = os.path.join(root, "../images")
rose_path = os.path.join(img_dir, "rose.png")

rose = cv2.imread(rose_path, 0)

phi1 = 255
phi2 = 69
phi3 = 0

for i in range(0, 50):
    w = i/50.0

    r = np.multiply(255, np.sin(np.multiply(w, rose)+phi1))
    g = np.multiply(255, np.sin(np.multiply(w, rose)+phi2))
    b = np.multiply(255, np.sin(np.multiply(w, rose)+phi3))

    col_rose = cv2.merge([r, g, b])
    cv2.imwrite(os.path.join(img_dir, "2B/{}.png".format(w)), col_rose)





