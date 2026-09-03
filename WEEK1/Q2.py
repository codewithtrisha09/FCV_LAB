import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread(r"C:\Users\Trisha\Downloads\images.jfif")
if image is None:
    print("Failed to load the image")
    exit()
# x=100
# y=50
# b,g,r=image[y,x]
# print("Red: ",r)
# print("Green: ",g)
# print("Blue: ",b)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
def get_pixel(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        b,g,r=image[y,x]
        print("RGB: ",r,g,b)
cv2.imshow("Image",image)
cv2.setMouseCallback("Image",get_pixel)
cv2.waitKey(0)
cv2.destroyAllWindows()