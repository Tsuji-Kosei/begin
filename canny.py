import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("/Users/tsujikousei/Documents/rutelia/soccer.jpg",0)
#0はグレースケールという意味
edge = cv2.Canny(img,100,200)
plt.style.use('default')
fig=plt.figure()
ax1=fig.add_subplot(1,2,1)
ax2=fig.add_subplot(1,2,2)
ax1.imshow(img,cmap='gray')
ax2.imshow(edge,cmap='gray')
ax1.set_title('original image')
ax2.set_title('edge image')
plt.show()
