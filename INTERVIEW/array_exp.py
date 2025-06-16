
import array

# Array of signed integers
int_array = array.array('i', [1, 2, 3, 4, 5])
# int_array.append("hello") # This would raise a TypeError

# Array of floats
float_array = array.array('f', [1.0, 2.5, 3.7])

print(int_array)      # Output: array('i', [1, 2, 3, 4, 5])
print(float_array[0]) # Output: 1.0