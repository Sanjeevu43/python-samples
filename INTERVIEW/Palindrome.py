
def find_largest_palindrome_in_string(s_num):
    n = len(s_num)
    largest_palindrome_str = ""   
    max_palindrome_val = -1

    for i in range(n):
        for j in range(i, n): # j is the ending index (inclusive for substring character)
            substring = s_num[i : j+1]
            # Check if the substring is a palindrome
            if substring == substring[::-1]:
                # If it is, convert to an integer to compare its numerical value
                current_val = int(substring)
                if current_val > max_palindrome_val:
                    max_palindrome_val = current_val
                    largest_palindrome_str = substring
    
    if max_palindrome_val == -1: # Should not happen if string has at least one digit
        return None 
    return largest_palindrome_str

# The number string provided
number_str = "74818369192"

# Find the largest palindrome
result = find_largest_palindrome_in_string(number_str)

print(f"The original number string is: {number_str}")

if result:
    print(f"The largest palindrome number found within it is: {result}")

#########################################################################################
print('========================================================================================')
def findLargestPalindrome(num):
    num_str = str(num)
    length = len(num_str)
    largest_palindrome_no = 0

    for i in range(length):
        for j in range(i,length):
            sub_string = num_str[i:j+1]
            if sub_string == sub_string[::-1]:
                temp_value = int(sub_string)
                if temp_value>largest_palindrome_no:
                    largest_palindrome_no=temp_value
    
    if largest_palindrome_no == 0:
        print("No largest palindrome found in number")
    else:
         print(f"largest palindrome found in number is :{largest_palindrome_no}")

number = 74818369192
findLargestPalindrome(number)






