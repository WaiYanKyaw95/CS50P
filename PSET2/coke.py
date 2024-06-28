amount_due = 50
# insert_coin = 0
# change_owed = 0

# loop until you pay 50 cent
while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    insert_coin = int(input("Insert Coin: "))
    # checking the coins 25 or 10 or 5
    if insert_coin == 25 or insert_coin == 10 or insert_coin == 5:
        # tracking the change owed to the customer
        change_owed = insert_coin - amount_due
        amount_due = amount_due - insert_coin
    else:
        continue

print(f"Change Owed: {change_owed}")

