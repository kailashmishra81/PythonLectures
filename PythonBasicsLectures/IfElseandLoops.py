greeting="Good Morning"

## If-Else
if greeting==" Morning":
    print("Good Morning")
else:
    print("Good Night")
print(greeting + " code executed")


## For - loops
str=[1,2,3,4,5]
for x in str:
    print("X is ", x)

## Sum of natural numbers using for loop
summation=0
for x in range(1,11):  ## this means summation from 1 to 10
    summation=summation+x
print("Summation is " , summation)

##Printing values by jumping iterations
for x in range(1,11,2): print("Jumping iterations ", x)


### While loops ####
a=5
while a>0:
    print(a)
    a=a-1
print("End of loop")

### While loops with break statement ####
b=10
while b>0:
    print(b)
    if(b==5):
        break
    b=b-1
print("value of b is ", b)

### While loops with continue statement ####
d=20
while d>0:
    if(d==15):
        d = d - 1
        continue

    if(d==10):
        break
    print(d)
    d=d-1
print("End of this loop with continue statement")


