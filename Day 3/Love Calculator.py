print("Welcome to the Love Calculator !")
name1 = input("Enter your name.\n ")
name2  = input("Enter their name.\n ")

combine_str = name1 + name2
lower_str = combine_str.lower()

t = lower_str.count("t")
r = lower_str.count("r")
u = lower_str.count("u")
e = lower_str.count("e")

true = t+r+u+e

l = lower_str.count("l")
o = lower_str.count("o")
v = lower_str.count("v")
e = lower_str.count("e")

love = l+o+v+e

love_Score = int(str(true)+str(love))

if (love_Score < 10) or (love_Score > 90) :
    print(f"Your Score is {love_Score}%, you go together like coke and mentos")
elif (love_Score >= 40) or (love_Score <= 50) :
    print(f"Your Score is {love_Score}%, you are alright together")
else:
    print(f"This is your score {love_Score}%")