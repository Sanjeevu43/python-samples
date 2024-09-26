from paddleocr import PaddleOCR, draw_ocr
import pytesseract
import keras_ocr
from PIL import Image
from PIL import ImageFont
import pandas as pd
from glob import glob
from tqdm.notebook import tqdm
import matplotlib.pyplot as plt
import cv2
import numpy as np
import easyocr
plt.style.use('ggplot')

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
IMAGE_PATH = 'C:/Users/PenikalS/Desktop/RaFTS/NewRaFTS/SerialNoImages/1030 G8.png'
img = cv2.imread(IMAGE_PATH) 
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
img = cv2.fastNlMeansDenoising(thresh)
result =  pytesseract.image_to_string(img, lang='eng')

dt = pd.DataFrame(result, columns=['Text'])
print("""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""")
print(dt)

#print(result)