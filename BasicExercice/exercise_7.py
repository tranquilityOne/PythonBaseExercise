#Find the number of occurrences of a substring in a string
def count_str(statement,search_str):
     print("Given String: ", statement)
     count = 0
     str_len = len(search_str)
     for i in range(len(statement)):
        count += statement[i:i + str_len] == search_str
     return count
search_str = "C"
statement = "GAAABBBCCCDDDFFFBBAACC"
print(search_str,"appeared ", count_str(statement,search_str), "Times")