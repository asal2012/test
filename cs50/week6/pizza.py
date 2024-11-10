from tabulate import tabulate
import csv
import sys
try:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too few command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a csv File")
    else:
        with open(sys.argv[1],"r") as file:
            reader = csv.reader(file)
            table = tabulate(reader, headers="firstrow" , tablefmt="grid")
            print(table)
except(FileNotFoundError):
    sys.exit("File does not exist")