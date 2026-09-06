import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread(r"C:\Users\Trisha\Downloads\images.jfif")
if image is None:
    print("Failed to load the image")
    exit()
#log_trans=c*log(1+r)
c=255/np.log(1+float(np.max(image)))
log_trans=c*np.log(1+image) #cause log(0) not defined
log_trans=np.uint8(log_trans)

plt.subplot(1,2,1)
plt.imshow(image,cmap='gray')
plt.title('Original Image')
plt.axis("off")
plt.subplot(1,2,2)
plt.imshow(log_trans,cmap='gray')
plt.title('Log_transformed Image')
plt.axis("off")
plt.show()