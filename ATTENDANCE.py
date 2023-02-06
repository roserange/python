a=int(input("enter the no of working days"))
b=int(input("enter the no class attended"))
attendence_percentage=(b/a)*100
if(attendence_percentage>75):
    print("you are eligible-",attendence_percentage,"%")
else:
    print("your attendence percentage is below 75%;is there any medical issue")
    print("enter y for yes")
    print("enter n for no")
    medical_issue=input("enter your answer")
    if(medical_issue=="y"):
        print("you are eligible")
    elif(medical_issue=="n"):
        print("you are not eligible")
    else:
        print("invalid input")
