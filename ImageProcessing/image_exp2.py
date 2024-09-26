import cv2
import numpy as np
from PIL import Image

img_file = ''

img1 = cv2.imread(img_file)
print('******************Image Type:',type(img1))
print('******************Shape***************** :',img1.shape)

img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
#pil_image=Image.fromarray(img2)
print('******************Image Type:',type(img2))
print('******************Shape***************** :',img2.shape)

cv2.imwrite("./ImageProcessing/img2.png",img2)


img2 = Image.open(img_file)
#img2 = np.array(img2)
print('******************Image Type:',type(img2))
print('******************Shape***************** :',img2.size)