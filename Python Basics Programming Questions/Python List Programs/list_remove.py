#Python Remove From List
#We will make a list while declaring the variables then, the Python program removes elements from the list. Finally, the new list will be displayed on the screen.
my_list = ['C', 'Java', 'Python', 'HTML', 'Javascript']
print('List:', my_list)
my_list.remove('HTML') # removed HTML from the list
print('New list:', my_list)


#Python Remove Duplicates from List
#In the previous program, the list contains a unique element but in this program, we are getting a list that contains duplicate elements, then the remove() method only removes the first matching element.
my_list = ['C', 'Java', 'Python', 'Java', 'Javascript', 'Java']
print('List:', my_list)
my_list.remove('Java')
print('New list:', my_list)