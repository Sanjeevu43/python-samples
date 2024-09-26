# List Comprehensions provide an elegant way to create new lists. The following is the basic structure of a list comprehension:
# output_list = [output_exp for var in input_list if (var satisfies this condition)]

org_list = [1,2,3,4,5,6,7,8,9]
# Filter even and add numbers from org_list

even_list = []
# Traditional
'''
for i in org_list:
    if i % 2 == 0:
        even_list.append(i)
print('Even List : ',even_list) '''

# Comprehension
even_list = [output for output in org_list if output%2 == 0]
print('Even List : ', even_list)

def getEvenSquares(org_list : list):
    return [i**2 for i in org_list if i%2 == 0]
    
# even squares
even_list = getEvenSquares(org_list)
print('Even Squares List : ', even_list)

# ****************************************** #
# Using map() object
'''
map() provides an alternative approach that’s based in functional programming. 
You pass in a function and an iterable, and map() will create an object. 
This object contains the output you would get from running each iterable element through the supplied function.
'''

sal_list = [10000,20000,15000]
bonus = 1000

def getSalary(sal):
    return (sal+bonus)

final_sal = map(getSalary, sal_list)
print('Final Salary : ', list(final_sal))

# comprehenson 
final_sal1 = [getSalary(sal) for sal in sal_list]
print('Final Salary 1: ', final_sal1)

# ********************************************** #
# If we want to do filter the list then we add if condition at the end (if else won't work at the end)
# If we want to modify values in list then we use if else before for loop (only if won't work before the for loop)
# replace the values
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices1 = [i if i > 0 else 0 for i in original_prices]
print('Prices1 : ',prices1)
# filter the values
prices2 = [i for i in original_prices if i>0]
print('Prices2 : ',prices2)

# if else logic put in separate function

def getPrice(price):
    return price if price > 0 else 0

prices3 = [getPrice(i) for i in original_prices]
print('Prices3 : ', prices3)












