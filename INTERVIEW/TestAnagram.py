from collections import Counter
def checkAnagrams():
   #Collection.
   str1 = "listen"
   str2 = "silent"
   if(len(str1)==len(str2)):
     str1 = sorted(str1)
     str2 = sorted(str2)
     print(str1)
     print(str1)
     res = str1==str2
     print('Two Strings are Anagrams or not:', res)

checkAnagrams()

def checkAnagrams():   
   str1 = "listen"
   str2 = "silent"
   ctr1 = Counter(str1)
   ctr2 = Counter(str2)  
   print(f'Two Strings are Anagrams or not:{ctr1==ctr2}')

checkAnagrams()


def checkAnagrams():
   #Collection.
   str1 = "listen"
   str2 = "silent"
   l1 = list(str1).sort()
   print(l1)
   if(len(str1)==len(str2)):
     str1 = sorted(str1)
     str2 = sorted(str2)
     print(str1)
     print(str1)
     res = str1==str2
     print('Two Strings are Anagrams or not:', res)

checkAnagrams()

