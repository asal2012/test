from datetime import date
import inflect
import sys
p = inflect.engine()
def main():
    try:
        birthday = input("Date of birth: ")
        y,m,d = birthday.split("-")
        age = convert(y,m,d)
        num2word(age,"minutes")
    except:
        sys.exit("Invalid Date")

def convert(y,m,d):
    try:
        tday = date.today()
        bday = date(int(y),int(m),int(d))
        age = tday - bday
    except:
        sys.exit("Invalid Date")
    return age.days*1440

def num2word(num):
    word = p.number_to_words(num,andword="").capitalize()
    return word

if __name__ == "__main__":
    main()