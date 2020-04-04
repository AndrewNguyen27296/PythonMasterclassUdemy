number_array = "9,222.231:34332/232"

separator = ""
for char in number_array:
    if not char.isnumeric():
        separator = separator + char

print(separator)
