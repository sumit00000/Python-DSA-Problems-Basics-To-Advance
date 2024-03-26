# Convert ASCII to Text in Python
# We are using the chr() function to convert ASCII to string. Which is a built-in function in Python that accepts a specified Unicode (ASCII value) as an argument and returns the character.
# The syntax of chr() is:
# chr(num)
# Where num will be an integer value.
# chr() Parameters:
# chr() method takes a single parameter, an integer i. The valid range of the integer is from 0 through 1,114,111.
# Return value from chr():
# The chr() method returns a character whose Unicode point is num, an integer. If an integer is passed that is outside the range then the method returns a ValueError.
# Python program to conversion ASCII to string
# take list
l = [75, 110, 111, 119, 32, 80, 114, 111, 103, 114, 97, 109]
# printing list
print("List of ASCII value =", l)
# ASCII to string using naive method
string = ""
for num in l:
    string = string + chr(num)
# Printing string
print ("String:", str(string))


# Python Program to Convert ASCII to String
# This is yet another way to convert ASCII to string. This is just shorthand to the above program in which we compact the code using list comprehension. The list comprehension can help us iterating through the list.
# Python program to conversion ASCII to string
# take lis
l = [75, 110, 111, 119, 32, 80, 114, 111, 103, 114, 97, 109]
# printing list
print("List of ASCII value =", l)
# ASCII to string using join() + list comprehension
string = ''.join(chr(num) for num in l)
# Printing string
print ("String:", str(string))


# ASCII to Text in Python
# We are using the join() and map() function to convert ASCII to string. The map() is a built-in function that applies a function on all the items of an iterator given as input.
# Python program to conversion ASCII to string
# take list
l = [75, 110, 111, 119, 32, 80, 114, 111, 103, 114, 97, 109]
# printing list
print("List of ASCII value =", l)
# ASCII to string using join() + map()
string = ''.join(map(chr, l))
# Printing string
print ("String:", str(string))


