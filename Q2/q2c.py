import os
import numpy as np
import matplotlib.pyplot as plt
import cv2

root = os.getcwd()
img_dir = os.path.join(root, "../images")
rose_path = os.path.join(img_dir, "rose.png")

rose = cv2.imread(rose_path, 0)
range_max = [0.1, 0.2, 0.5, 1]

for i in range_max:
    phi1 = np.random.randint(0, 10000*i)/10000
    phi2 = np.random.randint(0, 10000*i)/10000
    phi3 = np.random.randint(0, 10000*i)/10000
    w = 0.01

    r = np.multiply(255, np.sin(np.multiply(w, rose)+phi1))
    g = np.multiply(255, np.sin(np.multiply(w, rose)+phi2))
    b = np.multiply(255, np.sin(np.multiply(w, rose)+phi3))

    col_rose = cv2.merge([r, g, b])
    cv2.imwrite(os.path.join(img_dir, "2C/{}.png".format(i)), col_rose)



