#Remove first n characters from a string
def remove_chars(str,n):
    print("The original string is",str)
    x = str[n:]
    return x
print(remove_chars("hello word!",2))
print(remove_chars("aabbbcccsssddd",5))