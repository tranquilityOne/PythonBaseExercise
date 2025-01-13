#Given two lists of numbers, write a Python code to create a new list 
#such that the latest list should contain odd numbers 
#from the first list and even numbers from the second list.

def combine_list(list_1,list_2):
    new_list = []
    for n in list_1:
        if n%2 == 0:
            new_list.append(n)
    for n in list_2:
        if n%2 != 0:
            new_list.append(n)
    return new_list
list_1 = [1,2,3,5,6,7,10]
list_2 = [10,12,16,18,20,11,13]
print("The list_1 is",list_1)
print("The list_2 is",list_2)
print("The combine list is",combine_list(list_1,list_2))