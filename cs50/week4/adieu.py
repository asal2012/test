import inflect
p = inflect.engine()
name_list = []

name_list = []
while True:
    try:
        name = input("name:")
        name_list.append(name)
    except EOFError:
        print()
        break
mylist = p.join((name_list))
print(f"Adieu, adieu, to {mylist}")