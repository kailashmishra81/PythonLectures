import os

path="E:\KailashMine\Instructions.txt"

if os.path.exists(path):
    print ("Path Exists")
    if os.path.isfile(path):
        print ("File is a text file")
    elif os.path.isdir(path):
        print ("File is a directory")

else:
    print ("Path not Exists")

## Opening and Reading a file
try:
   with open(path,"r") as file:
        print (file.read())
except:
    print ("File not exists")

## Writing to a file
path1="E:\\KailashMine\\abcl.txt"
text="How are you?"
try:
    with open(path1,"w") as file:
        file.write(text)
except:
    print ("File not exists")


## Appends to an existing file
path1="E:\\KailashMine\\abcl.txt"
text="\nHow are you? dear friend\n  Welcome back\n"
try:
    with open(path1,"a") as file:
        file.write(text)
except:
    print ("File not exists")


## Copying files
path2="E:\\KailashMine\\backup"
import shutil
shutil.copy(path1,path2) ##src,des
