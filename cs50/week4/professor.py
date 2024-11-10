import random
def main():
    level = get_level()
    counter = 0
    score = 0
    while counter < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        answer = input(f"{x} + {y} = ")
        if answer == str (x+y):
            counter +=1
            score +=1
        elif answer != str(x+y):
            counter2 = 0
            while counter2 < 2:
                print("EEE")
                answer = input(f"{x} + {y} = ")
                counter2+=1
            print(f"{x} + {y} = {int(x)+int(y)}")
            counter +=1
    print(f"Score : {score}")
        
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1,2,3]:
                continue
            else:
                break
        except:
            continue
    return level

def generate_integer(level):
    if level == 1:
        level = random.randint(0,9)
    elif level == 2:
        level = random.randint(10,99)
    elif level == 3:
        level = random.randint(100,999)
    return level

if __name__ == "__main__":
    main()