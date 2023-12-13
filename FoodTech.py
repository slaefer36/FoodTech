import random
print("Register")
user_name = input("UserName: ")
age = int(input("age: "))
print("hello " + (user_name))
print("Confirm this Info: ")
info = input(("you are ") + str(age) + " years old and your name is " + (user_name) + (" (yes/no) "))

if info.lower() != "yes":
    print("Goodbye")
    quit()

question = input("Hungry? (yes/no) ")
if question.lower() != "yes":
    print("Goodbye")
    quit()

low_calories = ["Salad and Tuna in water (450Cal)", "Avocado and Kale (150Cal)"]
medium_calories = ["3 Chicken breasts with 1 Cup of Rice (650Cal)", "2 Medium potatoes and a fish fillet (600Cal)"]
high_calories = ["Pizza (900Cal)", "Sushi (850Cal)", "Hamburger (1000Cal)", "Chilli (700Cal)", "Rib-eye Steak (800Cal)"]

user_input = input("choose your desired meal(low/medium/high calories): ")

if user_input.lower() == 'low calories':
    print(random.choice(low_calories))

elif user_input.lower() == 'medium calories':
    print(random.choice(medium_calories))

elif user_input.lower() == 'high calories':
    print(random.choice(high_calories))

low_calories_d = ["Apple (20Cal)", "Banana (30Cal)", "Pear (25Cal)"]
medium_calories_d = ["Strawberry and whipped cream (200Cal)", "Pineapple smoothie (350Cal)", "Popsicle (120Cal)"]
high_calories_d = ["Milkshake (700Cal)", "Ice Cream (550Cal)", "Cake (800Cal)", "Pancakes (750Cal)"]

question2 = input("any desserts? (yes/no) ")
if question2.lower() != "yes":
    print("Goodbye")
    quit()

user_input2 = input("low/medium/high calories: ")

if user_input2.lower() == "low calories":
    print(random.choice(low_calories_d))

if user_input2.lower() == "medium calories":
    print(random.choice(medium_calories_d))

if user_input2.lower() == "high calories":
    print(random.choice(high_calories_d))



print("bon appetit!")