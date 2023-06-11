print("Welcome to the rollercoster!")

height =  int(input("What is your height in cm ? \n"))

if height>=120:
    print("You can Ride the rollercoster")
    age = int(input("Please Enter Your age."))
    if age < 12:
        print("Your Ticket price is $5")
    elif age <= 18:
        print("Your Ticket price is $7")
    else:
        print("Your Ticket price is $12")  
else:
    print("You cannot ride the rollercoster")