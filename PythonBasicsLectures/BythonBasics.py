from win32com.servers import dictionary

print("Hello World")

a=5
print(a)

a,b,c=5,10.5,"Hello Python"
print(a,b,c)

print("The value of b is ",b)

print(type(b))
print(type(a))
print(type(c))

########################################
##Working with List

str=[2,7,8,77.66,"Hello"]
print(str[0])   ##prints the first value
print(str[-1])  ##prints last value
print(str[1:3])   ##prints from index 1 till 3

str.insert(1,"Hello Dear")  ## at specific index it inserts
print(str)
str.append("End")  ## inserts at the end
print(str)

str[1]="Hello Ravi"  ## updates the existing value at Index position
print(str)

del str[1]   ## deletes the value at the index position
print(str)


## Working with Tuples
a=("Hello","World",2,4.5)
print(a)
print(type(a))

#a[1] = "Hello"   ## This will throw error as Tuple is immutable
#print(a)

## Working with Dictionary
dict={"a":5 ,"b":6, 5:"bcd","d":"Hello"}
print(dict)
print(dict[5])
print(dict["d"])

##Creating a new dictionary
dictionary = {}
dictionary["firstname"] = "Ravi"
dictionary["lastname"] = "Kumar"
print(dictionary)
