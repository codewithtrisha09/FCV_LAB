import cv2
import numpy as np
import matplotlib.pyplot as plt
image=cv2.imread(r"C:\Users\Trisha\Downloads\images.jfif")
if image is None:
    print("Failed to load the image")
    exit()
scale=2
resized=cv2.resize(image,None,fx=scale,fy=scale)
cv2.imshow("Original Image",image)
cv2.imshow("Resized image",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
