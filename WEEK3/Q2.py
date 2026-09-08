import cv2
import numpy as np
import matplotlib.pyplot as plt
image=cv2.imread(r"C:\Users\Trisha\Downloads\images.jfif")
if image is None:
    print("Failed to load the image")
    exit()
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
sobelx=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
sobely=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
gx=cv2.filter2D(image,cv2.CV_64F,sobelx)
gy=cv2.filter2D(image,cv2.CV_64F,sobely)
gradient=np.sqrt(gx**2+gy**2)
gradient=np.uint8(np.clip(gradient,0,255))
plt.subplot(1,2,1)
plt.imshow(image,cmap='gray')
plt.title("Original Image")
plt.axis("off")
plt.subplot(1,2,2)
plt.imshow(gradient,cmap='gray')
plt.title("Gradient image")
plt.axis("off")

plt.tight_layout()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
