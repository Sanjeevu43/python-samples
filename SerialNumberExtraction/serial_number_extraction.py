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

#img_files = glob("C:/Users/PenikalS/Desktop/RaFTS/NewRaFTS/SerialNumberSampleImages/*")
img_files = glob('C:/Users/PenikalS/Desktop/RaFTS/NewRaFTS/SerialNoImages/*')
#print(img_fnas)

#img_name = img_fnas[0].split('/')[-1].split('.')[0] #('.png')
'''
print(img_files[0].split('/'))
img_name = img_files[0].split('/')[-1].split('\\')[-1].rstrip('.png')
print(img_name)

fig ,axs = plt.subplots(2,3, figsize=(20,20))
axs = axs.flatten()
for i in range(6):
    axs[i].imshow(plt.imread(img_files[i]))
    axs[i].axis('off')
    iimg_name = img_files[0].split('/')[-1].split('\\')[-1].rstrip('.png')
    axs[i].set_title(img_name)
plt.show() '''

# Paddle
dfs = []
ocr = PaddleOCR(use_angle_cls=True, lang='en', show_log=True)
for img in tqdm(img_files[:2]):
    result = ocr.ocr(img, cls=False)
    img_name = img.split('/')[-1].split('\\')[-1].rstrip('.png')
    texts = [line[1][0] for line in result[0]]
    img_df = pd.DataFrame(result[0], columns=['bbox','text'])
    #img_df = pd.DataFrame(texts, columns=['texts'])
    img_df['img_name'] = img_name
    dfs.append(img_df)

paddleocr_df = pd.concat(dfs)
#print(paddleocr_df)

def paddle_result(img_file, paddleocr_df):
    img_name = img_file.split('/')[-1].split('\\')[-1].rstrip('.png')
    
    paddleocr_res = paddleocr_df.query('img_name == @img_name')[['text','bbox']].values.tolist()
    paddleocr_res = [(x[0][0],np.array(x[1])) for x in paddleocr_res]
    keras_ocr.tools.drawAnnotations(plt.imread(img_file),paddleocr_res)
    plt.title(img_name)
    plt.show()

for img_file in img_files[:2]:
    paddle_result(img_file, paddleocr_df)
# Tesseract
tesseract_result = {}
index =0 
for img in tqdm(img_files[:5]):
    result =  pytesseract.image_to_string(img, lang='eng')
    #print(type(result))
    img_name = img.split('/')[-1].split('\\')[-1].rstrip('.png')
    '''
    img_df = pd.DataFrame(result, columns=['texts'])
    img_df['img_name'] = img_name
    dfs.append(img_df) '''
    tesseract_result[index] = {'texts':result,'img_name':img_name}
    index = index+1

#tesseract_df = pd.concat(dfs)
tesseract_df = pd.DataFrame(tesseract_result)
#print(tesseract_df)
#print(tesseract_result)

# Keras
pipeline = keras_ocr.pipeline.Pipeline()
read_img =  keras_ocr.tools.read(img_files[0])
result = pipeline.recognize([read_img])
#print('Length : ',len(result))
dt = pd.DataFrame(result[0], columns=['Test','Boxes'])
#print(dt)

pd.set_option('display.max_rows', None)
dfs = []
pipeline = keras_ocr.pipeline.Pipeline()
for img in tqdm(img_files[:5]):
    read_img =  keras_ocr.tools.read(img)
    result = pipeline.recognize([read_img])
    img_name = img.split('/')[-1].split('\\')[-1].rstrip('.png')
    texts = [line[0] for line in result[0]]
    img_df = pd.DataFrame(result[0], columns=['text','bbox'])
    img_df['img_name'] = img_name
    dfs.append(img_df)

keras_df = pd.concat(dfs)
#keras_df

# EasyOCR
dfs = []
reader = easyocr.Reader(['en'])
for img in tqdm(img_files[:1]):    
    result = reader.readtext(img)
    img_name = img.split('/')[-1].split('\\')[-1].rstrip('.png')
    print('RES11 : ',result)
    #texts = [line[0] for line in result[0]]
    img_df = pd.DataFrame(result, columns=['bbox','text','con_score'])
    img_df['img_name'] = img_name
    dfs.append(img_df)
easyocr_df = pd.concat(dfs)
print("====================================EasyOCR======================================")
print(easyocr_df)

def image_compare(img_files, paddleocr_df, keras_df):
    img_name = img_files.split('/')[-1].split('\\')[-1].rstrip('.png')
    fig ,axs = plt.subplots(1,2, figsize=(10,10))    
    paddleocr_res = paddleocr_df.query('img_name == @img_name')[['text','bbox']].values.tolist()   
    new_paddleocr_res = [(x[0][0],np.array(x[1])) for x in paddleocr_res]
    print('RES3:', new_paddleocr_res)
    keras_ocr.tools.drawAnnotations(plt.imread(img_files),new_paddleocr_res,ax=axs[0])
    axs[0].set_title('paddleocr result', fontsize=24)

    keras_res = keras_df.query('img_name == @img_name')[['text','bbox']].values.tolist()
    new_keras_res = [(x[0],np.array(x[1])) for x in keras_res]
    keras_ocr.tools.drawAnnotations(plt.imread(img_files),new_keras_res,ax=axs[0])
    axs[1].set_title('kerasocr result', fontsize=24)
    plt.title('')
    plt.show()

image_compare(img_files[0], paddleocr_df, keras_df)


'''
ocr = PaddleOCR(use_angle_cls=True, lang='en', show_log=True)
#IMAGE_PATH = 'C:/Users/PenikalS/Desktop/RaFTS/NewRaFTS/SerialNumberSampleImages/Elitebook 845 G7.png' #1030 G8.png'
IMAGE_PATH = 'C:/Users/PenikalS/Desktop/RaFTS/NewRaFTS/SerialNoImages/1030 G8.png'
result = ocr.ocr(IMAGE_PATH, cls=False)

dt = pd.DataFrame(result[0], columns=['Boxes','Text'])
print(dt)

result = result[0]
image = Image.open(IMAGE_PATH).convert('RGB')
font = ImageFont.load_default()
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores, font_path='C:/Users/PenikalS/Desktop/RaFTS/NewRaFTS/Fonts/latin.ttf')
#im_show = draw_ocr(image, boxes, txts, scores, font_path='C:/Users/PenikalS/Desktop/RaFTS/NewRaFTS/Fonts/chinese_cht.ttf')
im_show = Image.fromarray(im_show)
im_show.save('sn_result.jpg') 

print('===================================================================================================')

img = cv2.imread(IMAGE_PATH) #C:\PythonExps\SimpleExps\OCR\ClearCode.PNG
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
img = cv2.fastNlMeansDenoising(thresh)
#print(img)

recognizedText = pytesseract.image_to_string(img)
print(recognizedText)

img = np.array(img)
cv2.imwrite('sn_result1.png', img) '''