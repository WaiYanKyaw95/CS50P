def main():
    output = get_fraction()
    if 0.25 <= output <= 0.75:
        print("{:.0f}%".format(output * 100))
    elif output <= 0.01:
        print("E")
    else:
        print("F")


def get_fraction():
    while True:
        # prompt user for an input (fraction) in the following format x/y
        userPrompt = input("Fraction: ")

        try:
            x, y = userPrompt.split("/")
            fraction = int(x) / int(y)
        # catch the following errors:
        #   1 DivisionError because of y = 0
        #   2 ValueError because of casting float number to integers
        #   3 TypeError because of casting string characters to integers
        except (ZeroDivisionError, ValueError, TypeError) as e:
            pass
        else:
            # ensure that x is less than y
            if fraction > 1:
                continue
            else:
                return fraction

main()


