import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread(r"C:\Users\Trisha\Downloads\images.jfif")
if image is None:
    print("Failed to load the image")
    exit()
c=1
gamma=0.5
r=image/255.0

power_transform=c*(np.power(r,gamma))
power_transform=np.uint8(power_transform*255)
plt.subplot(1, 2, 1)
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(power_transform, cmap="gray")
plt.title("Power-Law Image")
plt.axis("off")

plt.tight_layout()
plt.show()
