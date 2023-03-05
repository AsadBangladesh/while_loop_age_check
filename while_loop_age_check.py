#age check for driving license
while 1:
    user_age = int(input("Enter age : "))

    if user_age >=18 and user_age <=45:
        print("Your are eligible for driving license")

    elif user_age >=45:
        print("Your age too high")

    elif user_age <18:
        print("Your age too shot")