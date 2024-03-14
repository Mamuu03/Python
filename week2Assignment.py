#Creating an empty list
my_list=[]
#Append elements on my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
print(f'Appended list: {my_list}')
#Insert 15 at the second position in the list
my_list.insert(1,15)
print(f'my_list after inserting 15: {my_list}')
#Extend my_list with another list
list=[50,60,70]
my_list.extend(list)
print(f'my_list after extending another list: {my_list}')
#Remove the last element from my_list
del my_list[-1]
print(f'my_list after removing the last element: {my_list}')
#Sort my_list in ascending order
my_list.sort()
print(f'Sorted list: {my_list}')
#Find and print the index of the value 30 in my_list
my_list=my_list.index(30)
print(f'Index of value 30: {my_list}')
