import string
import re # re means regular expression module
import numpy as np
from sklearn import metrics
# To remove special chars in text. string.punctuation contains all special chars

print(string.punctuation)

def remove_specialchars(text):
    for pun in string.punctuation:
        if pun != '&':
            text = text.replace(pun,"")  
    text = text.lower()
    return text

testText = 'Welcome to #$%& "Python" @*+-(){Sanjeevu:;'
result = remove_specialchars(testText)
print(result)

##############################################
# x = df.iloc[:,0] ===> will take all rows of first column
# y = df.iloc[:,1] ===> will take all rows of second column

#metrics.accuracy_score

def text_process(text:str, process=True) -> str:
    if process:
        for pun in string.punctuation:
            if pun != '&':
                text = text.replace(pun,"")        
        text = text.lower()
        return text
    else:
        return text

result = text_process(testText,False)
print(result)

def remove_specialchars(text):
    if (len(text) != 0):
        allowedChars = ["&","-","'"]
        for pun in string.punctuation:
            if pun not in allowedChars:
                text = text.replace(pun,"")

        text = text.replace("\n","")
        return text

    else :
        return text

text = "@#$%San&Co-'\n\n"
#text = ""
result = remove_specialchars(text);
print("Res : ", result)

a_string = '!hi. wh?at &-is the weat[h]er lik?e.'
new_string = a_string.translate(str.maketrans('', '', string.punctuation))

print(new_string)
allowedChars = ["&","-","'"]
print(allowedChars)

def remove_chars(text):
    if (len(text) != 0):
        remove_chars = [",",":","'",">"]
        for remove_char in remove_chars:
            if remove_char in text:
                 text = text.replace(remove_char,"")       

        text = text.replace("\n","")
        return text

    else :
        return text
    
str9 = "San:jee>u, Nai'du"
res = remove_chars(str9)
print(res)



