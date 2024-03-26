# Python Program for Average of Numbers in a List
# In this program, we are using the For Loop to calculate the sum of numbers in a list. we can also take the help of a function to find the average of numbers in a list. A function is a block of code that performs a specific task. len() function is used to get the length or the number of elements in a list.
# Python program to calculate the average of numbers in a given list
def find_Average(n):
    sum_num = 0
    for i in n:
        # calculate sum of numbers in list
        sum_num = sum_num + i        
    # calculate average of numbers in list
    avg = sum_num / len(n)
    return avg
# take list
l = [5, 3, 8, 20, 15]
# calling function and display result
print('The average of list = %0.2f' %find_Average(l))


# In the previous program, inputs are hardcoded in the program but in this program, inputs will be provided by the user.
def find_Average(n):
    sum_num = 0
    for i in n:
        sum_num = sum_num + i        
    avg = sum_num / len(n)
    return avg
# total number you want to enter
n = int(input('How many numbers: '))
#take list
l = []
for i in range(n):
    l.append(float(input('Enter number: ')))
print('The average of list = %0.2f' %find_Average(l))


# Python Average Function
# We can calculate the average of numbers in the list by simply using the sum() and len() function. sum() will return the sum of all the numbers in the list, which can be divided by the number of elements returned by the len() function.
# Python program to calculate the average of numbers in a given list
def find_Average(n):
    # calculate average of numbers in list
    return sum(n) / len(n)
# take list
l = [4, 3, 15.5, 20, 17]
# calling function and display result
print('The average of list = %0.2f' %find_Average(l))


# Python Mean of List
# The mean() function in the python statistics library can be used to directly compute the average of a list.
# Python program to calculate the average of numbers in a given list
#importing mean() function
from statistics import mean
def find_Average(n):
    # calculate average or mean
    return mean(n)
# take list
l = [25, 50, 14, 63, 48, 53]
# calling function and display result
print('The average of list = %0.2f' %find_Average(l))


# Python Average of List using reduce() and lambda
# The reduce() to reduce the loop and by using the lambda function can compute summation of the list. The reduce() function is basically used to apply a particular(input) function to the set of elements passed to the function.
# Python program to calculate the average of numbers in a given list
#importing reduce() function
from functools import reduce
def find_Average(n):
    # calculate average of numbers in list
    return reduce(lambda x, y: x + y, n) / len(n)
# take list
l = [15, 13, 17, 2, 17]
# calling function and display result
print('The average of list = %0.2f' %find_Average(l))


# Python Average of Numbers in a List using numpy.average() methods
# The numpy.average() method is used to calculate the average of numbers in the list.
# Python program to calculate the average of numbers in a given list
#importing numpy() module
import numpy
def find_Average(n):
    # calculate average of numbers in list
    return numpy.average(n)
# take list
l = [2, 5, 10, 21, 4, 25]
# calling function and display result
print('The average of list = %0.2f' %find_Average(l))