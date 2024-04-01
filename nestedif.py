user = input ("Enter username :")
if user == "admin":
    print("You are successfully login in admin dasborad ")
    attendence = input ("enter attendence : ")
    if attendence == "full":
        print("staff attendence is full ")
    elif attendence == "half":
        print ("staff attendence is half ")
    elif attendence == "morning":
        print("staff attendence is morning")
    else:
        print("staff is absent")
else:
    print("you are not admin")
   


