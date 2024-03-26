# Swap Two Elements in a List Python
# Here, we will see how to swap two elements using the user-defined function, a user-defined function is a function that is defined by the user. In the code below we swap elements in the same list.
# Program description:- Write a python program to swap two elements in a list
# Python program to swap two elements in a list
# user-defined function
def swap(l, p1, p2):
   l[p1], l[p2] = l[p2], l[p1]
   return l
l = [1, 2, 3, 4, 5] # take inputs
# print list
print("List:", l)
# print new list
p1, p2 = 1, 2
print("New List:", swap(l, p1-1, p2-1))


# Another example of How to Swap Two Elements in a List Python.
# python program to swap two elements in a list
# user-defined function
def swap(l, p1, p2):
   l[p1], l[p2] = l[p2], l[p1]
   return l
# take inputs
l = [1, 2, 3, 4, 5]
# print list
print("List:", l)
# print new list
p1, p2 = 2, 4
print("New List:", swap(l, p1-1, p2-1))



# Python Program to Swap Two Elements in a List
# In the previous program, swap positions of elements are hardcoded in the program but in this program, the positions will be given by the user.
# python program to swap two elements in a list
# user-defined function
def swap(l, p1, p2):
   l[p1], l[p2] = l[p2], l[p1]
   return l
l = [5, 6, 7, 8, 9]  #take input
# print list
print("List:", l)
# take swap position of elements
p1 = int(input("Enter Position 1 Element: "))
p2 = int(input("Enter Position 2 Element: "))
# print new list
print("New List:", swap(l, p1-1, p2-1))


# Program to Swap Two Elements in a List Python
# This python program performs the same task but in different methods. Here, will see a code to swap the first and last element in list Python. We swap elements in list python by taking elements from the user.
# In the code, we have initialized new to an empty list, and also we are taking input from the user and storing it in n, then in the for loop, we take inputs for list elements and append it to empty list new.
# python program to swap two elements in a list
# take inputs
new = []
n = int(input("Enter number of elements in the list: " ))
for i in range(0, n):
   ele = int(input("Enter list element " + str(i+1) + ": " ))
   new.append(ele)
print(new)
# swap elements
temp = new[0]
new[0] = new[n-1]
new[n-1] = temp

# print new list
print("Swapped list:  ")
print(new)