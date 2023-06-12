import random

name_string = input("Give me everbody's names, seprated by comma. ")
names = name_string.split(", ")

num_items = len(names)
random_choise = random.randint(0,num_items-1)
person_will_pay = names[random_choise]

print(person_will_pay + " is going to pay")