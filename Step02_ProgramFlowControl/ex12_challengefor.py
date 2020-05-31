quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
upper_array = ""
for char in quote:
    if char.isupper():
        upper_array = upper_array + " " + char

print(upper_array)
