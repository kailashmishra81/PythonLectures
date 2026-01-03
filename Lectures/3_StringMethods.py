name="python Automation Class"

print(len(name))  ##Length of the string
print(name.find("o"))   ## Returns the first occurence
print(name.find("o", name.find("o") + 1))  ## Returns the second occurence
print(name.find("Auto")) ## Returns the first occurence of the substring
print(name.index("Auto")) ## Returns the first occurence of the substring

## Key differences between Index and Find
print(name.find("Auto1")) ## Returns -1 is the occurence is not found
#print(name.index("Auto2"))  ## Raises a exception like ValueError: substring not found

print(name.capitalize()) ##It will capitalize the first character of the string
print(name.isalpha())  ## will check ifts its an alphabet string
print(name.upper())
print(name.lower())
print(name.replace("o","w"))
print(name * 7)


