import os
import numpy as np
import matplotlib.pyplot as plt
import cv2

root = os.getcwd()
img_dir = os.path.join(root, "../images")
rose_path = os.path.join(img_dir, "rose.png")

rose = cv2.imread(rose_path, 0)

phi1 = np.random.randint(0, 255)
phi2 = np.random.randint(0, 255)
phi3 = np.random.randint(0, 255)
w = np.random.randint(0, 10**5)/ 10**5

print("W={0}\nPhi1={1}\nPhi2={2}\nPhi3={3}".format(w, phi1, phi2, phi3))
r = np.multiply(255, np.sin(np.multiply(w, rose)+phi1))
g = np.multiply(255, np.sin(np.multiply(w, rose)+phi2))
b = np.multiply(255, np.sin(np.multiply(w, rose)+phi3))

col_rose = cv2.merge([r, g, b])
cv2.imwrite(os.path.join(img_dir, "2A/colored.png"), col_rose)



