#Python Program to Create List of Numbers
#To create a list of numbers just mention the elements of the number inside the list declaration.
list = [1, 2, 3, 4, 5]
print(list)


#Python Program to Create List of Strings
#To create a list of strings just method the string elements inside the list within the quotes.
list = ["abc", "cdf", "rfg"]
print(list)


#How to Create Empty List in Python
#To create an empty list just initialize the list variable to square brackets without any elements in it.
list = [ ]
print(list)


#How to Create a List in Python from User Input
#We can directly take list elements from the user, so we create an empty list and ask the user to input list or string elements accordingly and then use for loop to append the elements into the list.
list = []
a = int(input("Enter number of elements: "))
for i in range(0, a):
   element = int(input())
   list.append(element) 
print(list)


#How to Create a 2d Array in Python
#To create a 2d array in python we need rows and columns, in the below code we have initialized n and m to 5 that is n represents row and m represents column, then by using for insert the elements.
n, m = (5, 5)
array = [[1 for i in range(n)] for j in range(m)]
print(array)


#Create a List in Python using For Loop
#Now let us use for loop to create a list of squares numbers in the range of 10. In the code, we have created an empty list and in for loop, we have used a range of 10 that is the list elements will have only 10 elements than by using the append() method we append the elements.
list = []
for i in range(10):
   list.append(i * i)
print(list)


#Create a List in Python using While Loop
#We can create a list in a while loop by specifying the length of the list that is How To Create A List In Python With Length. When we specify the length of the lit it prints the elements lesser than that length.
list = []
i = 0
while len(list) < 5:
   list.append(i)
   i += 1
print(list)


#Python Program to Create List from Range
#We specify the starting and ending range of the list by using the range function. ‘*’ is an unpacking operator which unpacks the range and prints the range elements.
list = [*range(1, 12)]
print(list)


#How to Take List as Input in Python in Single Line
#Now we will print the list in a single line by taking input from the user.
list = input('Type separated by space: ').split()
print(list)