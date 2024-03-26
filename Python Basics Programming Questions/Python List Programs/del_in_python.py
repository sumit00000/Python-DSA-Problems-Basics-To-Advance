#del Function in Python
#Here, we will develop a python program to delete user-defined objects. First, we will take a user-defined object then, we have to delete My_Project using the del My_Project statement.
# Python program to delete user-defined object
# user-defined object
class My_Project:
    x = 5
    def func(self):
        print('Know Program')

# Output
print(My_Project)
# deleting My_Project
del My_Project
# check if class exists
print(My_Project)


#Python delete Variable
# Python program to delete variable
# take variable
var = 25
# deleting variable
del var
# check if class exists
print(var)


#del List in Python
# Python program to delete list
my_list = ['Know Program', 'Python', 8, 'Java', 25,]
# deleting list
del my_list
# check if class exists
print(my_list)

#Python del Dictionary
# Python program to delete dictionary
# take dictionary
my_dict = {'Know Program', 'Python', 8, 'Java', 25,}
# deleting dictionary
del my_dict
# check if class exists
print(my_dict)


#Python del Tuples
# Python program to delete tuples
# take tuples
my_tuple = (5, 10, 15, 20, 25)
# deleting tuple
del my_tuple
# check if class exists
print(my_tuple)


#Python Delete Element from List
#The del statement can be used to delete an item or element at a given index.
# Python program to delete element from list by index
# take list
my_list = ['C', 'Java', 'Python', 'HTML', 'Javascript']
# printing original list
print('List:', my_list)
# removed first item from the list
del my_list[0]
# print list after item deletion
print('New list:', my_list)


#The del operator will delete multiple items from the list using slicing. del[a : b] :- This method deletes all the elements in range starting from index ‘a’ till ‘b’ mentioned in arguments.
# Python program to delete item from list
# take list
my_list = ['C', 'Java', 'Python', 'HTML', 'Javascript']
# printing original list
print('List:', my_list)
# removed item from the list
del my_list[2:4]
# print list after item deletion
print('New list:', my_list)


#Remove Value from Dictionary in Python
# Python program to delete item from dictionary
# take dictionary
my_dict = { 'name': 'Guddu',  'age': 21,  'profession': 'Programmer'}
# printing original dictionary
print('Dictionary:', my_dict)
# removed item from the dictionary
del my_dict['profession']
# print dictionary after item deletion
print('New Dictionary:', my_dict)


#Python delete item from the Tuples
#The del statement can’t delete items or elements of tuples and strings. It’s because tuples and strings are immutables; objects that can’t be changed after their creation.
# Python program to delete item from tuples
# take tuples
my_tuple = (5, 10, 15, 20, 25)
# removed item from the tuple
del my_tuple[3]
# print tuple after item deletion
print(my_tuple)


