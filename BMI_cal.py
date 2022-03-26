height=float(input("enter height:"))
weight=float(input("enter weight:"))
height=height/100
BMI=weight/(height*height)
if(BMI>0):
    if(BMI<=16):
        print("you are severly underweight")
    elif(BMI<=18.5):
        print("you are underweight")
    elif(BMI<=25):
        print("you are healthy")
    elif(BMI<=30):
        print("you are overweight")
    else:
        print("you are severly overweight")
else:
    print("please enter valid input")
