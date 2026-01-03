def Hello(name,greeting,age):
    print("Hello",name,greeting,"Your age is",age)


Hello("Ravi","Greetings",21)


## Scope of a variable in a function
name="hello hello"
def func1():
    name="Hello"
    print(name)

func1()  ## will print local version of the variable
print(name)  ## will print the global version of the variable


## By using *args[] parameter
def func2(*args):
    print(args)
    sum=0
    for i in args:
        sum=sum+i
    print(sum)

func2(1,2,3,4)


## By using **kwargs
## **kwargs stands for keyword arguments.It lets a function accept any number of named (key=value) arguments.
## 👉 Inside the function, kwargs is just a dictionary.

def func3(**kwargs):
    print(kwargs)       ## prints a dictionary {'name': 'abc', 'age': 20, 'height': 12.6}
    for x,y in kwargs.items():  ## way of printing the output with kwargs
        print(x,y)

func3(name="abc",age=20,height=12.6)

## How can we print the output in a single line when i have a func4(name="Ravi",age=20 , email="kk@kk.com") like Ravi 20 kk@kk.com
def func4(**arguments):
    for x,y in arguments.items():
        print(y,end=" ")

func4(name="Ravi", age=20, email="kk@kk.com")

## Why do we need **kwargs?
## Problem without kwargs
## def user(name, age, city, role):
##    ...

## What if tomorrow you add: email,phone,department?..You’d have to change the function every time