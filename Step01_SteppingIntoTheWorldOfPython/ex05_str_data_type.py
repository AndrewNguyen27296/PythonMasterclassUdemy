Sample = "Norwegian Blue"

# Index
print(Sample[3])
print(Sample[4])
print(Sample[9])
print(Sample[3])
print(Sample[6])
print(Sample[8])

# Negative number
print(Sample[-1])

# Slicing
print(Sample[1:6])

# Slice in step
# System will print every 2 indexes
print(Sample[1:10:2]) #owga

# Slicing backward
print(Sample[::-1]) #eulB naigewroN

# Challenge slice
letters = "abcdefghijklmnopqrstuvwxyz"
# Create a slice that produces the characters qpo
print(letters[16:13:-1])
# Slice the string to produce edcba
print(letters[4::-1])
# Slice the string to produce last 8 character, in reverse order
print(letters[-1:-9:-1])