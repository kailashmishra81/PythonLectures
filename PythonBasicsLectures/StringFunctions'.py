## Indexing with a string ##
from regex import split

text = "Python"
print(text[1:3])

str="KailashMishra@gmail.com"
str2="KailashMishra@gmail.com"
str1="Kailash"

print (str1 in str)  ## verifies is the text contains in the string or not

print(str[0:5])  ## extracts the substring

var=str2.split("@") ## separates the strings based upon the literal
print(var)
print(var[0])
