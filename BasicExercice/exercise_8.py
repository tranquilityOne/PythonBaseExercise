#Check Palindrome Number
def check_palindrome_number(number):
    reverse_number = str(number)[::-1]
    if(number > 0 and str(number) == reverse_number):
        return True
    return False
number = 1232
print("The number is",number,"palindrome ",check_palindrome_number(number))