fruits = {"Apple" : 130, "Avocado" : 50, "Banana" : 110, "Cantaloupe" : 50,
"Grapefruit" : 60, "Grapes" : 90,"HoneydewMelon" : 50, "Kiwifruit" : 90,
"Lemon" : 15,"Lime" : 20, "Nectarine" : 60, "Orange" : 80, "Peach" : 60, "Pear" : 100, "Pineapple" : 50,
"Plums" : 70, "Strawberries" : 50, "Sweet Cherries" : 100, "Tangerine" : 50, "Watermelon" : 80}

user_input = input("item:").title()
while True:
    if user_input in fruits:
        print(fruits[user_input])
        break