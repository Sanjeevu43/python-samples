
# Creating a dictionary with string keys and list values
my_dict = {
    "fruits": ["apple", "banana", "cherry"],
    "vegetables": ["carrot", "potato", "broccoli"],
    "colors": ["red", "green", "blue"],
    "animals": ["dog", "cat", "elephant"],
    "countries": ["USA", "Canada", "Mexico"]
}

# Removing the first element of each list in the dictionary
for key in my_dict:
    if my_dict[key]:  # Check if the list is not empty
        my_dict[key].pop(0)

# Display the modified dictionary
print(my_dict)

{
    "fruits": ["banana", "cherry"],
    "vegetables": ["potato", "broccoli"],
    "colors": ["green", "blue"],
    "animals": ["cat", "elephant"],
    "countries": ["Canada", "Mexico"]
}
