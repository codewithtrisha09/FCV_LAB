import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread(r"C:\Users\Trisha\Downloads\images.jfif")
if image is None:
    print("Failed to load the image")
    exit()

f=np.array([[10,20,30],[40,45,50],[55,60,65]])
h=np.array([[1,2,3],[4,5,6],[7,8,9]])
correlation_matrix=f*h
correlation=np.sum(correlation_matrix)
h_flip=np.flip(h)
convolution_matrix=f*h_flip
convolution=np.sum(convolution_matrix)
print("Image Neighbourhood")
print(f)
print("Filter Kernel")
print(h)
print("Correlation",correlation)
print("Convolution",convolution)

