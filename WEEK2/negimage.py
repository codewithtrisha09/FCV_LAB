import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread(r"C:\Users\Trisha\Downloads\images.jfif")
if image is None:
    print("Failed to load the image")
    exit()
negative_image=255-image
cv2.imshow("negative image",negative_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
