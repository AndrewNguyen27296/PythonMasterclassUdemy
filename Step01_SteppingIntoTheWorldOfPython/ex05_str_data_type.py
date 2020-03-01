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

# Region String Replacement Fields
age = 24
print("My age is " + str(age) + " years")
print("My age is {0} years".format(age))
# EndRegion

# Region Formatting
for i in range(1, 13):
    # 2,3,4 is the space, left
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i**2, i**3))
    # left, mid, center
    print("No. {0:2} squared is {1:<3} and cubed is {2:>4}".format(i, i ** 2, i ** 3))
# EndRegion

