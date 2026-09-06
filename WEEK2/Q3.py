import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread(r"C:\Users\Trisha\Downloads\images.jfif")
resized=cv2.resize(image,(400,300))
cropped=image[50:150,100:300]
plt.subplot(1,3,1)
plt.imshow(resized,cmap='gray')
plt.title("Resized Image")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(cropped,cmap='gray')
plt.title("Cropped Image")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(image,cmap='gray')
plt.title("Original Image")
plt.axis("off")
plt.tight_layout()
plt.show()