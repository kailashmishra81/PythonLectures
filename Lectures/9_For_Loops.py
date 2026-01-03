import time
## For - loops

print("*********************************************************")
str="Hello World"
for x in str:
    print(x)


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


## Printing a message like Happy New Year after completing countdown of 10 seconds
for x in range(10,0,-1):
    print(x)
    time.sleep(1)
print("Happy New Year")