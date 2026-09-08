import cv2
import numpy as np
import matplotlib.pyplot as plt
image=cv2.imread(r"C:\Users\Trisha\Downloads\images.jfif")
if image is None:
    print("FAILED TO LOAD THE IMAGE")
    exit()
r1=90
r2=180
s1=0
s2=255
mapping=np.zeros(256,dtype=np.uint8)
for r in range(256):
    if r<=r1:
        mapping[r]=((s1/r1)*r)
    elif r<=r2:
        mapping[r]=((s2-s1)/(r2-r1))*(r-r1)+s1
    else:
        mapping[r]=((255-s2)/(255-r2))*(r-r2)+s2
piecewise=mapping[image] # type: ignore

plt.subplot(1,2,1)
plt.imshow(piecewise,cmap='gray')
plt.title("Piecewise transformation")
plt.axis("off")
plt.subplot(1,2,2)
plt.imshow(image,cmap='gray')
plt.title("Original Image")
plt.axis("off")
plt.tight_layout()
plt.show()

