import os
import cv2
import numpy as np

path = '/home/haliltezel/Desktop/origin'
mask_path = '/home/haliltezel/Desktop/masked'
for filename in os.listdir(path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image = cv2.imread(os.path.join(path, filename))
        height, width = image.shape[:2]
        mask = np.zeros((height, width), dtype=np.uint8)
        cv2.imwrite(os.path.join(mask_path, "mask_" + filename), mask)