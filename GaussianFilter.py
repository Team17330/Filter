import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('pun.jpg',0)

blur1 = cv2.GaussianBlur(img,(3,3),0)
blur2 = cv2.GaussianBlur(img,(3,3),21)
blur3 = cv2.GaussianBlur(img,(7,7),0)
blur4 = cv2.GaussianBlur(img,(7,7),21)

plt.subplot(151),plt.imshow(img,'gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(152),plt.imshow(blur1,'gray'),plt.title('3x3, sig=0')
plt.xticks([]), plt.yticks([])
plt.subplot(153),plt.imshow(blur2,'gray'),plt.title('3x3, sig=21')
plt.xticks([]), plt.yticks([])
plt.subplot(154),plt.imshow(blur3,'gray'),plt.title('7x7, sig=0')
plt.xticks([]), plt.yticks([])
plt.subplot(155),plt.imshow(blur4,'gray'),plt.title('7x7, sig=21')
plt.xticks([]), plt.yticks([])
plt.show()
