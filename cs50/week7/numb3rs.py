import re
def main():
    print(validate(input("IPv4 Address:")))

def validate(ip):
    try:
        a,b,c,d = ip.split(".")
        if int(a) > 255 or int(b) > 255 or int(c) > 255 or int(d) > 255:
            return False
        else:
            pattern = re.search(r"^\d+\.{1}\d+\.{1}\d+\.{1}\d+$",ip)
            if pattern:
                return True
            else:
                return False
    except ValueError:
        return False
    
if __name__ == "__main__":
    main()