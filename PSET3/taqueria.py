def main():
    totalAmount(menu)

def totalAmount(l):
    # initialize total amount
    n = 0

    while True:
        try:
            item = input("Item: ").title()
        except EOFError: # catching eof error if you type in ctrl + d into the prompt
            break
        else:
            for i in l: # loop through the dictionary
                if item == i:
                    n += l[i] # adding the amount of items from the menu
                    print("Total: $" + "{:.2f}".format(n)) # print the total amount with two decimal places

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

main()
