# Python program to remove element from list by index


#pop() Function in Python
#We will take the list while declaring the variables then, the Python program removes the given index element from the list. Finally, the new list will be displayed on the screen.
my_list = ['C', 'Java', 'Python', 'HTML', 'Javascript']
print('List:', my_list)
my_list.pop(3)    # removed index 3 item from the list
print('New list:', my_list)



#Python List pop() last
#The argument passed to the method is optional. If not passed, the default index -1 is passed as an argument (index of the last item).
# Python program to remove item from list
my_list = ['C', 'Java', 'Python', 'HTML', 'Javascript']
print('List:', my_list)
my_list.pop()  # removed item from the list
print('New list:', my_list)


#Python pop() IndexError
#If the index passed to the method is not in range, then the remove() method is getting IndexError: pop index out of range.
# Python program to remove item from list
my_list = ['C', 'Java', 'Python', 'HTML', 'Javascript']
print('List:', my_list)
my_list.pop(8)  # removed index 8 item from the list
print('New list:', my_list)