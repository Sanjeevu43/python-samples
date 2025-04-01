import test
def m1():
    print('OK')

m1()

# l1 = ['Hello',1,2]
# l2 = ['Hello',2,1]
# print(l1==l2)
# print(l1 is l2)
print('**************************************************************************************88')
# s1 = 'Hello'
# s2 = 'Hello'
# print(s1==s2)
# print(s1 is s2)

# s1 = '''Highly experienced and results-oriented IT professional with 18 years in the industry, with the last 3 years specializing in 
# Optical Character Recognition (OCR), Machine Learning, and Generative AI. Proven ability to design, develop, and deploy innovative solutions 
# using technologies such as EasyOCR, Tesseract OCR, TrOCR, PaddleOCR, PyTorch, Scikit-Learn, Python, LLMs, FastAPI, and Streamlit. 
# My background includes extensive experience in full-stack Java development using Spring, Hibernate, and REST APIs, along with front-end expertise 
# in HTML, JavaScript, Angular, and ReactJS. Passionate about leveraging cutting-edge technologies to solve complex business problems and drive 
# impactful results. Eager to contribute expertise and leadership to a challenging and rewarding role.
# '''
# s2 = '''Highly experienced and results-oriented IT professional with 18 years in the industry, with the last 3 years specializing in 
# Optical Character Recognition (OCR), Machine Learning, and Generative AI. Proven ability to design, develop, and deploy innovative solutions 
# using technologies such as EasyOCR, Tesseract OCR, TrOCR, PaddleOCR, PyTorch, Scikit-Learn, Python, LLMs, FastAPI, and Streamlit. 
# My background includes extensive experience in full-stack Java development using Spring, Hibernate, and REST APIs, along with front-end expertise 
# in HTML, JavaScript, Angular, and ReactJS. Passionate about leveraging cutting-edge technologies to solve complex business problems and drive 
# impactful results. Eager to contribute expertise and leadership to a challenging and rewarding role.
# '''
# print(s1==s2) #True
# print(s1 is s2) #True

tpl1 = ('Hello',1,2)
tpl2 = ('Hello',1,2)
print(tpl1==tpl2)
print(tpl1 is tpl2)

def create_tuple():
    return ('Hello', 1, 2,3)

tpl1 = ('Hello', 1, 2,3)
tpl2 = create_tuple()  # Dynamically created tuple

print(tpl1 == tpl2)  # True
print(tpl1 is tpl2)  # Likely False

tpl1 = ('Hello',1,2,[4,5,6])
tpl2 = ('Hello',1,2,[4,5,6])
print(tpl1==tpl2)
print(tpl1 is tpl2)