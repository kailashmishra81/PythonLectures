temperature=int(input("Enter temperature Outside: "))
##Logical AND OR operators
if(temperature>0 and temperature<=30):
    print("Temperature is good outside")
elif(temperature<=0 or temperature>30):
    print("Temperature is bad outside")

##NOT operators
AQI=int(input("Enter AQI: "))
if not(AQI>=0 and AQI<=100):
    print("AQI is bad outside")
elif not(AQI>=100):
    print("AQI is good outside")
elif(AQI == 0):
    print("AQI is UNIMAGINABLE")