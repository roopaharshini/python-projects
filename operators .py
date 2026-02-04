# Operators in Python - Example Program

a = 10
b = 3

# Arithmetic Operators
print("Arithmetic Operators")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)
print("a ** b =", a ** b)
print("a // b =", a // b)
print()

# Relational (Comparison) Operators
print("Relational Operators")
print("a > b =", a > b)
print("a < b =", a < b)
print("a == b =", a == b)
print("a != b =", a != b)
print("a >= b =", a >= b)
print("a <= b =", a <= b)
print()

# Logical Operators
print("Logical Operators")
print("a and b =", a and b)
print("a or b =", a or b)
print("not a =", not a)
print()

# Assignment Operators
print("Assignment Operators")
c = a
print("c =", c)

c += b
print("c += b ->", c)

c -= b
print("c -= b ->", c)

c *= b
print("c *= b ->", c)

c //= b
print("c //= b ->", c)
print()

# Bitwise Operators
print("Bitwise Operators")
print("a & b =", a & b)
print("a | b =", a | b)
print("a ^ b =", a ^ b)
print("a << 1 =", a << 1)
print("a >> 1 =", a >> 1)
print()

# Membership Operators
print("Membership Operators")
nums = [1, 2, 3, 10]
print("10 in nums =", 10 in nums)
print("5 not in nums =", 5 not in nums)
print()

# Identity Operators
print("Identity Operators")
x = a
y = b
print("x is a =", x is a)
print("x is not b =", x is not b)

# Conditional (Ternary) Operator
print("\nConditional Operator")
result = "a is greater" if a > b else "b is greater"
print(result)
