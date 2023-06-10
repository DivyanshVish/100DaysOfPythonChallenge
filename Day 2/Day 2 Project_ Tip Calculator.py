# Tip Calculator

print("Welcome to Tip Calculator !")
bill = float(input("What was the Total Bill ? $ "))
tip = int(input("What percentage tip would like to give ? 10 , 12 or 15 ? "))
people = int(input("How many people to split the bill ? "))

tip_per = tip /100
total_tip_amt = bill * tip_per
total_bill = bill + total_tip_amt
bill_per_people = total_bill / people
final_amt = round(bill_per_people,2)

print(f"Each Person should pay $ {final_amt}")