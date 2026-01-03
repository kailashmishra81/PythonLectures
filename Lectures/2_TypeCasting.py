## Type casting with Python

a=10
b=12.5
c="1600"

##
print(type(a))
print(type(b))
print(type(c))

##print("Value of a"+ a)  ## Here the error will appear because of TyeCasting issue
print("Value of a:", str(a))  ## Now here is type casted to String type

print("## Here we are type casting values of a,b and c to Int type")
print(int(b))
print(int(c))

print("## Here we are type casting values of a,b and c to Float type")
print(int(a))
print(int(c)*10)

print("## Here we are type casting values of a,b and c to String type")
print(str(a))
print(str(b))
print(c * 10)
