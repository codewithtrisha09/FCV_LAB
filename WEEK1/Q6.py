import cv2
import numpy as np
import matplotlib.pyplot as plt
image=cv2.imread(r"C:\Users\Trisha\Downloads\images.jfif")
if image is None:
    print("Failed to load the image")
    exit()
rotated=cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Original",image)
cv2.imshow("Rotated image",rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()