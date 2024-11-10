buy_list = {}
while True:
    try:
        item = input().upper()
        if item in buy_list:
            buy_list[item] += 1

        else:
            buy_list[item] = 1
    except (EOFError , KeyError):
        break
for i in sorted(buy_list):
    print(buy_list[i],i)