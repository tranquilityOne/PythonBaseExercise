str = "PYnative"
index = 0
print("Orginal String is ",str)
print("Printing only even index chars")
print("-----solution %-----")
for s in str:
    index = index + 1
    if index%2 != 0:
        print(s)
    
print("-----solution slice-----")
newStr = str[::2]
for s in newStr:
        print(s)

print("-----solution range-----")
len = len(str)
for s in range(0,len,2):
        print(str[s]) 