# String to ASCII in Python
# We will discuss how to convert each character in a string to an ASCII value. We are using the ord() function to convert a character to an integer (ASCII value). Which is a built-in function in Python that accepts a char (a string of length 1) as an argument and returns the Unicode code point for that character. We can use this function to find the ASCII value of any character.
# Python program to find ASCII value of each character in string
# take input
string = input("Enter any string: ")
# printing ascii value of each character
for i in range(len(string)):
    print("The ASCII value of character %c = %d" %(string[i], ord(string[i])))


# ASCII Value of String in Python
# This is yet another way to find the ASCII value of each character in a string. This is just shorthand to the above program in which we compact the code using list comprehension.
# Python program to find ASCII value of each character in string
# take input
string = input("Enter any string: ")
# find ascii value using list comprehension
ASCII_value = [ord(ch) for ch in string]
# printing ascii value of each character
print("The ASCII value of characters:", ASCII_value)


# Sum of ASCII Values of String in Python
# In the previous program, we will find the ASCII value of each character in a string but in this program, we will develop a Python program to find the sum of ASCII values of all characters in a string.
# Python program to find ASCII value of string
# take input
string = input("Enter any string: ")
# find ascii value of string
ASCII_value = sum(ord(ch) for ch in string)
# printing ascii value
print("The ASCII value of characters:", ASCII_value)


# Python Program to Find String to ASCII
# We are using the sum() and map() function to find the sum of ASCII values of all characters in a string. map() is a built-in function that applies a function on all the items of an iterator given as input.
# Python program to find ASCII value of string
# take input
string = input("Enter any string: ")
# find ascii value of string
ASCII_value = sum(map(ord, string))
# printing ascii value
print("The ASCII value of characters:", ASCII_value)