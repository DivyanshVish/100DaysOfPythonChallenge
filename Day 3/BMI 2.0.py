#BMI Calculator 2.0

height  = float(input("Enter Your Height \n"))
weight  = float(input("Enter Your Weight \n"))

bmi = round(weight/height**2)

if bmi<18.5:
    print(f"Your BMI {bmi}, You are Under Weight")
elif 18.5<=bmi<25:
    print(f"Your BMI {bmi}, You are Normal Weight")
elif 25<=bmi<30:
    print(f"Your BMI {bmi}, You are OverWeight")
elif 30<=bmi<35:
    print(f"Your BMI {bmi}, You are Obese")
else:
    print(f"Your BMI {bmi}, You are Clinically Obese")