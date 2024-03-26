# Python Subtraction Between Two Lists
# We will take two lists while declaring the variables. Then, convert the list to set using set() function and subtract sets. Finally, the subtraction value will be displayed on the screen. The set() function creates a set object. The items in a setlist are unordered, so they will appear in random order.
# Python program to subtract two lists
# take list
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [1, 3, 4, 7, 9]
# print original list
print('list1 =', a)
print('list2 =', b)
# subtraction of list
sub = list(set(a) - set(b))
# print subtraction value
print('list1 - list2 =', sub)


# Subtract Two arrays
# In the previous program, we used the set() function but in this program, we will subtract 2 lists without using the set() function.
# Python program to subtract two lists
# take list
a = [10, 20, 30, 40, 50, 60, 70, 80, 90]
b = [20, 30, 60, 80]
# print original list
print('list1 =', a)
print('list2 =', b)
# subtraction of list
sub = [i for i in a if not i in b or b.remove(i)]
# print subtraction value
print('list1 - list2 =', sub)


# Python Subtract Lists Element by Element
# In this program, we will give two lists. Then, subtract all elements present in the list and store them in a sub variable using the For Loop. Finally, the subtraction value will be displayed on the screen.
# Python program to subtract lists element by element
# take list
a = [20, 25, 30, 40, 55, 15]
b = [5, 12, 35, 40, 45, 28]
# print original list
print('list1 =', a)
print('list2 =', b)
# subtraction of element
sub = []
for i in range(len(a)):
    sub.append(a[i] - b[i])
# print subtraction value
    

# Subtract All Elements in Array
# This python program also performs the same task but with different methods. In this program, we are using a built-in function. The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together, etc.
# Python program to subtract lists element by element
# take list
a = [20, 25, 30, 40, 55, 15]
b = [10, 35, 30, 26, 67, 12]
# print original list
print('list1 =', a)
print('list2 =', b)
# subtraction of element
sub = [x-y for (x, y) in zip(a, b)]
# print subtraction value
print('list1 - list2 =', sub)


# Subtract Function in Python
# The numpy.subtract() function is used when we want to compute the difference of two numbers or arrays. It returns the difference of numbers.
# Python program to subtract lists element by element
# importng numpy.subtract()
import numpy
# take list
a = [10, 14, 8, 64, 54, 47]
b = [10, 33, 45, 12, 54, 23]
# print original list
print('list1 =', a)
print('list2 =', b)
# subtraction of element
sub = numpy.subtract(a, b)
# print subtraction value
print('list1 - list2 =', sub)