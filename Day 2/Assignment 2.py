age = input("What is Your age ?\n")

age_as_int = int(age)

year_left = 90 - age_as_int

day = year_left * 365
weeks = year_left * 52
months  = year_left * 12

print(f"Your have {day} days, {weeks} weeks and {months} months left.")