print("Welcome to the rollercoster!")

height =  int(input("What is your height in cm ? \n"))
bill = 0
if height>=120:
    print("You can Ride the rollercoster")
    age = int(input("Please Enter Your age. "))
    if age < 12:
        bill = 5
        print("Children Ticket $5")
    elif age <= 18:
        bill = 7
        print("Youth Ticket $7")
    elif age >= 45 and age <= 55 :
        print("Have a Free Ride on the House !")
    else:
        bill = 12
        print("Adult Ticket $12")  
    wanna_photo = input("do you want to take Photo taken ? Y or N ")
    if wanna_photo == "Y":
        bill += 3
    print(f"Your Final Bill is ${bill}")
else:
    print("You cannot ride the rollercoster")