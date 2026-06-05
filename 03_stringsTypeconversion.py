"""
Strings takes some extra space in memory
"""

print(ord('A')) # ASCII value of A
print(chr(66)) # Character represented by ASCII value 66

# indexing, the first character is at index 0
s = "Hello"
print(s[0]) # H
print(s[1]) # e
print(s[2]) # l
print(s[3]) # l
print(s[4]) # o
# print(s[5]) # IndexError: string index out of range

#String slicing
print(s[0:2]) # He
print(s[1:4]) # ell
print(s[:3]) # Hel
print(s[2:5]) # llo
print(s[:]) # Hello

"""
in string slicing, the first index is inclusive and the second index is exclusive.
"""

print(s[0:5:2]) # Hlo
print(s[::2]) # Hlo
print(s[1:5:2]) # el
print(s[1::2]) # el

"""
The third parameter in string slicing is called step. It is used to skip characters in the string. The default value of step is 1, which means that it will not skip any characters. If we set step to 2, it will skip every other character in the string.
"""

# type conversion
num = 123
num_str = str(num) # convert integer to string
print(num_str) # '123'
print(type(num_str)) # <class 'str'>

num_str = "123"
print(type(num_str)) # <class 'str'>

is_python_fun = True
bool_num = int(is_python_fun) # convert boolean to integer
print(bool_num) # 1
print(type(bool_num)) # <class 'int'>

# the above conversions are explicit conversions, we can also do implicit conversions in some cases. For example, when we concatenate a string with an integer, the integer will be implicitly converted to a string.

num = 10
str_num = "The number is " + str(num) # implicit conversion of num to string
print(str_num) # The number is 10