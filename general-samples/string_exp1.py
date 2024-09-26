word = "Hello"

print(word[2])
print(word[:2])
print(word[2:])

msg = "HELLO WORLD"

new_msg = msg.casefold().capitalize()
print(new_msg)
print("------------------------")
name = "Alice"
age = 30
#formatted_text = "My name is {} and I am {} years old.".format(name, age)
formatted_text = f"My name is {name} and I am {age} years old."
print(formatted_text)  # Output: "My name is Alice and I am 30 years old."

msg1 = " HELLO "
print(len(msg1))
#new_msg1 = msg1.lstrip()  # will remove beginning white space (before)
#new_msg1 = new_msg1.rstrip() # will remove end white space (after)
new_msg1 = msg1.strip() # will remove both ls and rs
print(new_msg1)
print(len(new_msg1))

msg2 = "Malayalam"

new_msg2 = msg2[::-1]
print(new_msg2)

text = "Hello, world! 👋"
# Encode using UTF-8
encoded_text = text.encode('utf-8')
print(encoded_text)  # Output: b'Hello, world! \xe2\x98\xba' (bytes in UTF-8 format)

# Encode using ASCII (will raise an error since it can't handle emoji)
try:
    encoded_ascii = text.encode('ascii')
except UnicodeEncodeError:
    print("Error: Can't encode emoji in ASCII")

# Decode back to a string
decoded_text = encoded_text.decode('utf-8')
print(decoded_text)  # Output: Hello, world! 👋



