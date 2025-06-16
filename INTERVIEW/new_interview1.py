
s = 'Hello'
print(s)
#s=reversed(s)
s1="".join(reversed(s))
print(type(s))
print(type(s1))

for i in s:
    print(i)

print(s1)

def reverse_string_with_reversed(s):
    return "".join(reversed(s))

my_string = "hello"
reversed_str = reverse_string_with_reversed(my_string)
print(f"Original: {my_string}")
print(f"Reversed: {reversed_str}") # Output: olleh

s12="Helloacvb"

s123=sorted(s12,reverse=True)
print(s123)

l=[1,2,3]
print(sum(l))
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@222')
name1 = 'Hello'
name1 = "".join([name1,'1'])
print(name1)