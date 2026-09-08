import cv2
import numpy as np
import matplotlib.pyplot as plt
image=cv2.imread(r"C:\Users\Trisha\Downloads\images.jfif")
if image is None:
    print("Failed to load the image")
    exit()
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
box=cv2.boxFilter(image,-1,(5,5))
gaussian=cv2.GaussianBlur(image,(5,5),0)
plt.subplot(1,3,1)
plt.imshow(image,cmap='gray')
plt.title("Original Image")
plt.axis("off")
plt.subplot(1,3,2)
plt.imshow(box,cmap='gray')
plt.title("Box Filtered Image")
plt.axis("off")
plt.subplot(1,3,3)
plt.imshow(gaussian,cmap='gray')
plt.title("Gaussian Filtered Image")
plt.axis("off")
plt.tight_layout()
plt.show()
