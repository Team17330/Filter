import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('pun.jpg',0)

kernel1 = np.ones((3,3),np.float32)/9
blur1 = cv2.filter2D(img,-1,kernel1)
kernel2 = np.ones((7,7),np.float32)/49
blur2 = cv2.filter2D(img,-1,kernel2)

plt.subplot(131),plt.imshow(img,'gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(blur1,'gray'),plt.title('Box Filter 3x3')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(blur2,'gray'),plt.title('Box Filter 7x7')
plt.xticks([]), plt.yticks([])
plt.show()
