a = 1
b = 3

# These 2 return same number
print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 * 12))

# These 3 return same number
print((((a + b) / 3) - 4) * 12)
print(((a + b) / 3 - 4) * 12)

c = a + b
d = c / 3
e = d - 4
print(e*12)

# PEMDAS Parentheses, Exponents, Mul/Div, Add/Sub
# BEDMAS Brackets, Exponents, Mul/Div, Add/Sub
# BODMAS Brackets, Order, Mul/Div, Add/Sub
# BIDMAS Brackets, Index, Mul/Div, Add/Sub
# => Div and Mul has same level
# => If mixed operations, they're evaluated from left to right
