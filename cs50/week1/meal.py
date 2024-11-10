def main():
    x = input("what time is it?")
    if 7 <= convert(x) <=8:
        print("breakfast time")
    elif 12 <= convert(x) <=13:
        print("launch time")
    elif 18 <= convert(x) <=19:
        print("dinner time")
    else:
        print("")


def convert(time):
    x, y = time.split(":")
    x = float(x)
    y = float(y) / 60
    return x + y


if __name__ == "__main__":
    main()