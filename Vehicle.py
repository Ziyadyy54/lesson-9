print("choose your type of transportation ")
print("1. 2 wheeler")
print("2. 4 wheeler")
inputno1=int(input("enter your choice of transportation "))
if(inputno1==1):
    print("what type of 2 wheeler do you want")
    print("1. bike")
    print("2.scooter")
    print("3.hover board")
    inputno2=int(input("give your answer "))
    if (inputno2==1):
        print("you choose bike")
    elif (inputno2==2):
        print("you choose scooter")
    elif (inputno2==3):
        print("you choose hover board")
    else:
        print("invalid input")
elif(inputno1==2):
    print("what type of 4 wheeler do you want")
    print("1. sedan")
    print("2.SUV")
    print("3.mini van / van")
    inputno2=int(input("give your answer "))
    if (inputno2==1):
        print("you choose sedan")
    elif (inputno2==2):
        print("you choose SUV")
    elif (inputno2==3):
        print("you choose mini van / van")
    else:
        print("invalid input")
else:
    print("you have entered an invalid input")