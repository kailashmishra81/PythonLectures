## Slicing = create a substring by extracting the elements from another string
## With slice :: [start:stop:step]

str1="Hello Little World"
print(str1[6:12])  ## Will print Little. Indexing starts at 0 index and excludes the last index for stop.

## this way we can reverse a string in Python by passing step as negative
print(str1[17::-1])

length=len(str1)
print(str1[length::-1])

print(str1[0:18:2])  ## Prints "HloLtl ol". Picks every 2nd character.

## Say we want to extract google from this string
##This is the first approach
Str2="www.google.com"
Str3=Str2[4:10]
print(Str3)

##But say if you want to extract the domain name from any website.Then this code will work for all
Str4=input("Enter website name: ")
print("Website entered is",  Str4)
Str5=Str4[4::]
print("The substring is",Str5)
length2=len(Str5)
print("The length of the substring is",length2)
Str6=Str5[:length2-4:]
print("The domain is",Str6)

