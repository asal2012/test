import sys
import csv
table = []
with open(sys.argv[1],"r") as file:
    reader = csv.DictReader(file)
    for student in reader:
        l,f = student["name"].split(", ")
        table.append({"first":f, "last":l, "house":student["house"]})