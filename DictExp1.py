import collections
people = {'ID_3': "Jim", 'ID_2': "Jack", 'ID_4': "Jane", 'ID_1': "Jill",'ID_10': "July"}

print(people)
od1 = collections.OrderedDict(sorted(people.items()))
print(od1)

print('******************************************************************************')

people1 = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}
print(people1)
od = collections.OrderedDict(sorted(people1.items()))
print(od)


x = 755
x1 = x//5
x2 = x1%5

print('X1=', x1)
print('X2=', x2)

# initializing empty dictionary
test_dict = {}
 
# printing original dictionary
print("The original dictionary : " + str(test_dict))
print("Length: ", len(test_dict))
 
# using not operator
# Check if dictionary is empty
res = len(test_dict) == 0
 
# print result
print("Is dictionary empty ? : " + str(res))

test_list = []
# using not operator
# Check if dictionary is empty
res = not test_list
#res = len(test_dict) == 0
 
# print result
print("Is List empty ? : " + str(res))
if not test_list:
    print("List not empty")

config_new = {}
config = {'loaded_model': 'resources/CEDAR1v4model1nocanvas30epochs.hdf5', 
          'data_generator': 'resources/SignatureDataGenerator_CEDAR1v4model1nocanvas.pkl', 
          'multi_anchor_model': 'min_score_rule', 'threshold_too_light': 0.99, 'threshold_too_dark': 0.6, 
          'match_method': 'Correlation', 'hog_cellsize': 16, 'threshold_match': -1.0, 'account_audit': True, 
          'feature_extraction': False, 'debugging': False}

config_new = config

print(config)
print('========================================')
print(config_new)


