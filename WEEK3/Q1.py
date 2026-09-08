import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread(r"C:\Users\Trisha\Downloads\images.jfif")

if image is None:
    print("Failed to load the image")
    exit()
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
blur=cv2.GaussianBlur(image,(5,5),0)
mask=cv2.subtract(image,blur)
sharp=cv2.add(image,mask)
plt.subplot(1,2,1)
plt.imshow(image,cmap='gray')
plt.title("Original Image")
plt.axis("off")
plt.subplot(1,2,2)
plt.imshow(sharp,cmap='gray')
plt.title("Sharpened Image")
plt.axis("off")
plt.tight_layout()
plt.show()

