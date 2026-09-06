import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread(r"C:\Users\Trisha\Downloads\images.jfif")
if image is None:
    print("Failed to load the image!")
    exit()

img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
equalized=cv2.equalizeHist(img)
cv2.imshow("HISTOGRAM EQUALIZED IMAGE",equalized)
cv2.imshow("Original Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()