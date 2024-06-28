def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 2 <= len(s) <= 6 and s[0:2].isalpha():
        zero_count = 0
        digit_count = 0
        for c in s:
            if c.isdigit() and c == '0' and zero_count == 0:
                return False
            elif c.isdigit() and c != '0':
                zero_count += 1
                digit_count += 1
            elif c.isdigit() == False and digit_count >= 1:
                return False
            else:
                continue
    else:
        return False

    return True

main()

# “All vanity plates must start with at least two letters.”
#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end.
# For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
# The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”


