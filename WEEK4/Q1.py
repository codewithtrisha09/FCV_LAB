import cv2
import numpy as np
import matplotlib.pyplot as plt
image=cv2.imread(r"C:\Users\Trisha\Downloads\images.jfif")
if image is None:
    print("Failed to load the image")
    exit()
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
T=127
binary=np.zeros_like(gray)
for i in range(gray.shape[0]):
    for j in range(gray.shape[1]):
        if gray[i,j]>T:
            binary[i,j]=255
        else:
            binary[i,j]=0
plt.subplot(1, 2, 1)
plt.imshow(gray, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(binary, cmap="gray")
plt.title("Binary Image")
plt.axis("off")

plt.tight_layout()
plt.show()