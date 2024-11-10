amount_due = 50
while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    pool = int(input("insert coin:"))
    if pool in (25,10,5):
        amount_due -= pool
    else:
        continue
print(f"Change owed: {abs(amount_due)}")