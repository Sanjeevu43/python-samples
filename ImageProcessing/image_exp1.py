import cv2
import numpy as np
from PIL import Image

# BGR means CV2 image
# RGB means PIL image

# cv2.COLOR_BGR2RGB means from CV2 to PIL
# cv2.COLOR_RGB2BGR means from PIL to CV2

# 1 To convert from OpenCV image to PIL image
opencv_image=cv2.imread("demo2.jpg") # open image using openCV2

# convert from openCV2 to PIL. Notice the COLOR_BGR2RGB which means that 
# the color is converted from BGR to RGB
color_converted = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
pil_image=Image.fromarray(color_converted)

# 2 To convert from PIL image to OpenCV use:

pil_image=Image.open("demo2.jpg") # open image using PIL
# use numpy to convert the pil_image into a numpy array
numpy_image=np.array(pil_image)  

# convert to a openCV2 image, notice the COLOR_RGB2BGR which means that 
# the color is converted from RGB to BGR format
opencv_image=cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR) 

# 3 way
img = cv2.imread("path/to/img.png")

# You may need to convert the color.
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
im_pil = Image.fromarray(img)

# For reversing the operation:
im_np = np.asarray(im_pil)

