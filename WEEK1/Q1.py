import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread(r"C:\Users\Trisha\Downloads\images.jfif")
if image is None:
    print("Failed to load the iamge")
    exit()

cv2.imshow("Original_Image",image)
cv2.imwrite("ogimg.png",image)
cv2.waitKey(0)
cv2.destroyAllWindows()