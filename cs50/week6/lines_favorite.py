fav_country = input("what is your favorite country? ")
fav_city = input("what is your favorite city? ")
fav_food = input("what is your favorite food? ")
fav_dessert = input("what is your favorite dessert? ")
fav_celebration = input("what is your favorite celebration? ")
fav_important_day = input("what is your favorite important day? ")
fav_place = input("where is your favorite place? ")
fav_thing = input("what is your favorite thing? ")
i = open("fav","a")
i.write(f"{fav_country},{fav_city},{fav_food},{fav_dessert},{fav_celebration},{fav_important_day},{fav_place},{fav_thing}")