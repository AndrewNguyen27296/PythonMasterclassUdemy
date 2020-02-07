# Region syntax_and_parameters

# syntax
# print(object(s), separator=separator, end=end, file=file, flush=flush)

# parameter values
# -----------------------------------------#
# Parameter               | Description                                                                                           |
# --------------------------------------------------------------------------------------------------------------------------------|
# objects                 | Any object, and as many as you like. Will be converted to string before printed                       |
# sep = 'separator'       | Optional. Specify how to separate the objects, if there is more than one. Default is ' '              |
# end = 'end'             | Optional. Specify what to print at the end. Default is '\n' (line feed)                               |
# file                    | Optional. An object with a write method. Default is sys.stdout                                        |
# flush                   | Optional. A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False |

# EndRegion

# print more than 1 objects
print('Hello World', 'how are you?')

# print a tuple
tuple = ("a", "b", "c")
print(tuple)

# print two messagesm and specify the separator:
print("Hello", "how are you?", sep=", ")
