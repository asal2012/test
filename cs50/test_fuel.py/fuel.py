def main():
    while True:
        try:
            fraction = input("Fraction: ") #1/2 #1/4 #2/3
            p = convert(fraction)
            x = gauge(p)
            print(x)
        except(ValueError, ZeroDivisionError):
            continue

def convert(fraction):
    x,y = fraction.split("/")
    x = int(x)
    y = int(y)
    p = (x/y)*100
    return p

def gauge(percentage):
    if 0 <= percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        x = str(percentage)+"%"
    return x

if __name__ == "__main__":
    main()