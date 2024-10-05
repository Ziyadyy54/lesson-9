healthissue=input("did you have medical issues yes or no ")
attendance=float(input("enter the attendance of the student "))
if(healthissue)=="yes":
    print("you are allowed")
else:
    if(attendance)>=75:
        print("you are allowed ")
    else:
        print("sorry but you have failed to maintain the minimum attendance")