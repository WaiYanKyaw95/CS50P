# import inflect library
# The methods of the class engine in module inflect.py provide plural inflections,
# singular noun inflections, “a”/”an” selection for English words, and manipulation of numbers as words.
import inflect

p = inflect.engine()

# initiate the list
nameList = []

# while true
while (True):
# ask for user input for the name - one name per line
# and append the new name to the list, using append() method
    try:
        name = input("Name: ")
        nameList.append(name)
# get out of the loop if user input control-d
# by catching the EOFError error
    except EOFError:
        print("")
        break

# use inflect.engine().join() method to format the string
nameList = p.join(nameList)

# print out the adieu string
print("Adieu, adieu, to " + nameList)