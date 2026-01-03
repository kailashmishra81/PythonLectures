# In Python Constructor overloading is not possible. Python only keeps the last definition and overrides the first one.
# If we have to call the default constructor then pass the default args as 0
# self keyword is mandatory for calling variable names into methods
# instance and class variables have completely different purposes
# constructor name should start with __init__
# new keyboard is not required to create new objects of the class


class Calculator:
    c=100
    def abc(self):
        print("I am in Calculator class")

    # def __init__(self):   ## This is the constructor declaration
    #     print("I am in __init__")
    def __init__(self,a=0,b=0):
        print("I am in __init__")
        self.a=a
        self.b=b
    def summation(self):
        return(self.a+self.b+self.c)

obj1=Calculator()
obj1.abc()
print(obj1.c)
#obj2=Calculator()
obj3=Calculator(5,6)
print("The Summation is ",obj3.summation())
obj3=Calculator(115,116)
print("The summation is ",obj3.summation())

print ("###################################")
