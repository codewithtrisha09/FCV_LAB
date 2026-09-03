import cv2
import numpy as np
import matplotlib.pyplot as plt
image=cv2.imread(r"C:\Users\Trisha\Downloads\images.jfif")
if image is None:
    print("Failed to load the image")
    exit()
cv2.rectangle(image,(50,50),(100,150),(0,255,0),2)
cv2.imshow("Rectangle",image)
cv2.waitKey(0)
cv2.destroyAllWindows()