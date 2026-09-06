import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread(r"C:\Users\Trisha\Downloads\images.jfif")
if image is None:
    print("Failed to load the image!")
    exit()

img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
equalized=cv2.equalizeHist(img)
cv2.imshow("HISTOGRAM EQUALIZED IMAGE",equalized)
cv2.imshow("Original Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# import cv2
# import matplotlib.pyplot as plt

# # Read image
# image = cv2.imread(r"C:\Users\Trisha\Downloads\images.jfif",0)

# # Histogram Equalization
# equalized = cv2.equalizeHist(image)

# # Display images
# plt.subplot(1, 2, 1)
# plt.imshow(image, cmap="gray")
# plt.title("Original Image")
# plt.axis("off")

# plt.subplot(1, 2, 2)
# plt.imshow(equalized, cmap="gray")
# plt.title("Equalized Image")
# plt.axis("off")

# plt.show()