# Arithmetic Operators

a = 10
b = 3

print("a + b =", a + b)  # Addition Results in 13
print("a - b =", a - b)  # Subtraction Results in 7
print("a * b =", a * b)  # Multiplication Results in 30
print("a / b =", a / b)  # Division Results in 3.3333333333333335
print("a % b =", a % b)  # Modulus Results in 1
print("a ** b =", a ** b)  # Exponentiation Results in 1000
print("a // b =", a // b)  # Floor Division Results in 3


# Comparison Operators
x = 5
y = 9

print("x == y:", x == y)  # Equal to
print("x != y:", x != y)  # Not equal to
print("x > y:", x > y)    # Greater than
print("x < y:", x < y)    # Less than
print("x >= y:", x >= y)  # Greater than or equal to
print("x <= y:", x <= y)  # Less than or equal to

# Logical Operators
p = True
q = False

print("p and q:", p and q)  # Logical AND
print("p or q:", p or q)    # Logical OR
print("not p:", not p)      # Logical NOT
print("not q:", not q)      # Logical NOT

# Assignment Operators
c = 5
print("Initial value of c:", c)
c += 2  # Equivalent to c = c + 2
print("After c += 2:", c)
c -= 1  # Equivalent to c = c - 1
print("After c -= 1:", c)
c *= 3  # Equivalent to c = c * 3
print("After c *= 3:", c)
c /= 2  # Equivalent to c = c / 2
print("After c /= 2:", c)
c %= 4  # Equivalent to c = c % 4
print("After c %= 4:", c)
c **= 2  # Equivalent to c = c ** 2
print("After c **= 2:", c)
c //= 3  # Equivalent to c = c // 3
print("After c //= 3:", c)

# Bitwise Operators
m = 5  # In binary: 0101
n = 3  # In binary: 0011

print("m & n:", m & n)  # Bitwise AND - Results in 1 (0001)
print("m | n:", m | n)  # Bitwise OR - Results in 7 (0111)
print("m ^ n:", m ^ n)  # Bitwise XOR - Results in 6 (0110)
print("~m:", ~m)        # Bitwise NOT - Results in -6 (in two's complement)
print("m << 1:", m << 1)  # Left Shift - Results in 10 (1010)
print("m >> 1:", m >> 1)  # Right Shift - Results in 2 (0010)

# Identity Operators
a = [1, 2, 3]
b = a  # b references the same list as a
c = [1, 2, 3]  # c is a different list with the same content
print("a is b:", a is b)  # True, because a and b reference the same object
print("a is c:", a is c)  # False, because a and c reference different objects
print("a == c:", a == c)  # True, because a and c have the same content

# Membership Operators
my_list = [1, 2, 3, 4, 5]
print("3 in my_list:", 3 in my_list)  # True, because 3 is in the list
print("6 in my_list:", 6 in my_list)  # False, because 6 is not in the list
print("3 not in my_list:", 3 not in my_list)  # False, because 3 is in the list
print("6 not in my_list:", 6 not in my_list)  # True, because 6 is not in the list

# Ternary Operator
age = 18
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)  # Output: Status: Adult

# Operator Precedence
result = 10 + 5 * 2  # Multiplication has higher precedence than addition
print("Result of 10 + 5 * 2:", result)  # Output: 20

# Parentheses can be used to change the order of evaluation
result = (10 + 5) * 2  # Parentheses change the order of evaluation
print("Result of (10 + 5) * 2:", result)  # Output: 30

# Chaining Comparison Operators
x = 5
print("1 < x < 10:", 1 < x < 10)  # True, because x is greater than 1 and less than 10
print("x >= 5 < 10:", x >= 5 < 10)  # True, because x is greater than or equal to 5 and less than 10