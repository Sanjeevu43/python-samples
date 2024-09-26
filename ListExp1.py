from queue import PriorityQueue


def workOnListOject():
    l1 = [1,2,3,[4,5,6]];
    l2 = [7,8,9]
    l3 = l1+l2
    l3.append(10)
    l3.insert(3,4)
    l3.remove(4)
    removedValue = l3.pop()
    print(removedValue)
    removedValue = l3.pop(3)
    print(removedValue)
    return l3;
print(workOnListOject())

list1 = [10,20,30];
list2 = [40,50,60];
list3 = [401,501,601];
list1.extend(list2)
list1.extend(list3)
print("list1 : ", list1)

list3 = [70,80,90];
list4 = [100,150,160];
list3.append(list4)
print(list3)
print(list4)

sortList = [1,2,4,6,5,8,9,3,7]
sortList.sort(reverse=True)
print(sortList)
#sortList.reverse()
#print(sortList)

findElement = 9 in sortList 
print(findElement)

findElement = sortList.count(9)
print(findElement)

print(sortList.index(5))
print(sortList[1])

names = ['San','Bindu','Lucky','Bittu'];
print(names.index('Lucky'))
name = 'Sanjeevu'
print('Length', len(name))
x = [4,2,1,3]
print(sum(x))

l = [1,1,2,3,4,5,5]
print('l type is : ', type(l))
print("l = ", len(l))
newl = list(set(l))
print("newl = ", list(newl))

names = ['Sany','Bittu','Bin','Lucky']
result = [name for name in names if name!='Sany']
print(result)

newl2 = list([1,2,3])

print('newl2 type is : ', type(newl2))

set1 = {1,2,3,4,4}
print(set1)
print('set1 type : ', type(set1))

text= 'Hello my Name is Sanjeev'
print(text.lower())
text_result = ''.join(text)
text = text.split()
print(text)
result=''
text_result1 = []
text_result2 = ''

for word in text:
    result = word.lower()
    text_result1.append(result)

text_result2 = ' '.join(text_result1)
print(text_result1)
print(text_result2)
    
ll1 = [1,2,3,4,5]

ll2 = [i for i in ll1 if i != 5]
print('ll2 = ', ll2)

ll3 = ['San','44']

name,age = ll3
print('Name :', name ,' Age :', age)
#print('Name :', name ,' Age : ', age)



