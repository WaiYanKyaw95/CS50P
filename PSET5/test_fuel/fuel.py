def main():
    # ask for user input in fraction
    fract = input("Fraction (X/Y): ")
    # convert it into number
    percent = convert(fract)
    # present it in percentage or E or F
    print(gauge(percent))

def convert(fraction):
    # expect input in X/Y format
    x, y = fraction.split("/")
    # if X and/or Y is not an integer
    if not(x.isdigit() or y.isdigit()):
        raise ValueError
    # if Y is zero
    elif int(y) == 0:
        raise ZeroDivisionError
    # if dividend is larger than divisor
    elif int(x) > int(y):
        raise ValueError
    # otherwise return x/y multiplied by 100 and round it into nearest number
    else:
        return round(int(x)/int(y) * 100)

def gauge(percentage):
    # tank full with F (over 99%)
    if percentage >= 99:
        return "F"
    # tank (almost) empty with E (under 1%)
    elif percentage <= 1:
        return "E"
    # print out the exact percentage of the fuel tank
    else:
        return '{:.0f}%'.format(percentage)
