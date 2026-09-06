import cv2
import numpy as np
import matplotlib.pyplot as plt

input_img=cv2.imread(r"C:\Users\Trisha\Downloads\hist_match_original_image.tif",0)
ref_image=cv2.imread(r"C:\Users\Trisha\Downloads\hist_match_ref_image.tif",0)

hist_input=cv2.calcHist([input_img],[0],None,[256],[0,256])
hist_ref=cv2.calcHist([ref_image],[0],None,[256],[0,256])

cdf_input=hist_input.cumsum()
cdf_ref=hist_ref.cumsum()

cdf_input=cdf_input/cdf_input[-1]
cdf_ref=cdf_ref/cdf_ref[-1]
mapping=np.zeros(256,dtype=np.uint8)
for i in range(256):
    mapping[i]=np.argmin(np.abs(cdf_ref-cdf_input[i]))

result=mapping[input_img]
plt.subplot(1, 3, 1)
plt.imshow(input_img, cmap="gray")
plt.title("Input Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(ref_image, cmap="gray")
plt.title("Reference Image")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(result, cmap="gray")
plt.title("Histogram Specified")
plt.axis("off")

plt.show()
