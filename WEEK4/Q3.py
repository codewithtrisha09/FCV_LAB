import cv2
import numpy as np
import matplotlib.pyplot as plt
image=cv2.imread(r"C:\Users\Trisha\Downloads\images.jfif")
if image is None:
    print("Failed to load the image")
    exit()
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
mask=np.zeros((image.shape[0],image.shape[1]),dtype=np.uint8)
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        R=image[i,j,0]
        G=image[i,j,1]
        B=image[i,j,2]

        if G>R*1.2 and G>B*1.2:
            mask[i,j]=255
        else:
            mask[i,j]=0
segmented=np.zeros_like(image)
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if mask[i,j]==255:
            segmented[i,j]=image[i,j]
plt.subplot(1,3,1)
plt.imshow(image,cmap='gray')
plt.title("Original Image")
plt.axis("off")
plt.subplot(1,3,2)
plt.imshow(mask,cmap='gray')
plt.title("Mask Image")
plt.axis("off")
plt.subplot(1,3,3)
plt.imshow(segmented,cmap='gray')
plt.title("Segmented Image")
plt.axis("off")
plt.tight_layout()
plt.show()