def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # vanity plates contain a number of between 2 and 6 (min and max), and start with two letters
    # No space, punctuation, period is allowed
    # the above conditions must be met
    if 2 <= len(s) <= 6 and s[0:2].isalpha() and s.isalnum():
        digit_count = 0
        for c in s:
            # the first number used cannot be a zero, and ensure that zero hasn't been there yet
            if c.isdigit() and c == '0' and digit_count == 0:
                return False
            # if it doesn't start with zero and if it's a digit, count the digit
            elif c.isdigit() and c != '0':
                digit_count += 1
            # numbers can't be used in the middle, they must come at the end
            elif c.isdigit() == False and digit_count >= 1:
                return False
    else:
        return False

    return True

if __name__ == "__main__":
    main()

# “All vanity plates must start with at least two letters.”
#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end.
# For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
# The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”


