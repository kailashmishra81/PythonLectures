name=""
while(len(name)==0):
    name=input("Please enter your name")

print("Welcome to Python",name )

##Another approach to do the same thing:
name=None
while not name:
    name=input("Please enter your name")
print("Welcome to Python World",name )

