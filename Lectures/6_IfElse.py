User_Input=int(input("What is your age ? "))

if User_Input==100:
    print("You are 100 years old")
elif User_Input >= 18 and User_Input < 100:
    print("You are 18 years or above 18 years old")
elif User_Input < 18 and User_Input > 0:
    print("You are below 18 years old")
elif User_Input==0:
    print("You are not yet born")
else:
    print("You are a super human")
