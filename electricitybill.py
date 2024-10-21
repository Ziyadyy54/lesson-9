kilowhttsused=int(input("enter the number of kilowatts used "))
if(kilowhttsused<50):
    amount=kilowhttsused*2.6
    tax=25
elif(kilowhttsused<100):
    amount=kilowhttsused*3.25
    tax=35
elif(kilowhttsused<200):
    amount=kilowhttsused*5.36
    tax=45
else:
    amount=kilowhttsused*9
    tax=75
total=amount+tax
print("the total is ",total)