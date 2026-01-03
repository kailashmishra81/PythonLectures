MyPhoneNumber="612-875-5305"

## In this program, using continue we are removing the occurence of this - character
for i in MyPhoneNumber:
    if(i=="-"):
        continue
    print(i,end="")

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
