"""
from collections import Counter

groceryList = []

def main():
    c = Counter(itemList(groceryList))
    for l in c:
        print(f"{c[l]} {l}")


def itemList(l):
    while True:
        try:
            item = input("")
        except EOFError:
            return groceryList
        else:
            l.append(item.upper())

main()
"""
# empty dictionary
groceryList = {}

def main():
    groceryHelper(groceryList)

def groceryHelper(l):
    while True:
        try:
            i = input().upper() #   input from user in all CAP
        except EOFError:
            break
        else:
            if i in l:  #   if the input item is already in the dict, then increment its value
                l[i] += 1
            else:       #   otherwise, initialize it with 1
                l[i] = 1

    for item in sorted(l):  #   sort the dict by its key
        print(f"{l[item]} {item}")

main()
