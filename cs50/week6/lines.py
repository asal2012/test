import sys
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 2:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".py"):
    sys.exit("not a python file")

try:
    with open(sys.argv[1],"r") as file:
        f = file.readlines()
        counter = 0
        for i in f:
            if i.lstrip().startswith("#"):
                continue
            elif i.lstrip() == "":
                continue
            else:
                counter+=1
    print(counter)
except(FileNotFoundError):
    sys.exit("file does not exist")