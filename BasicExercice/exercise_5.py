#Check if the first and last numbers of a list are the same
def first_last__same(number_list):
    first = number_list[0]
    last = number_list[-1]
    if first == last:
        return True
    else:
        return False
print(first_last__same([10,20,31,34,10]))
print(first_last__same([20,20,31,34,10]))