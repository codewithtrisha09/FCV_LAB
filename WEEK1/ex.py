import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread(r"C:\Users\Trisha\Downloads\images.jfif",0)
cv2.imshow("GrayScale Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("grayscaleimg.jpg",image)
