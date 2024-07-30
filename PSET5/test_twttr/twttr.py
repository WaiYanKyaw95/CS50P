# main function job is to ask for the input from users
# and use shorten function to shorten the user input text by removing any vowels.
def main():
    input_text = input("Input: ")
    print(f"Output: {shorten(input_text)}")

def shorten(word):
    # check every character in a word
    for c in word:
        # if they are vowels and ensure that both cap or small letters are captured.
        # and replace it with nothing or remove it.
        if c.lower() == 'a' or c.lower() == 'e' or c.lower() == 'i' or c.lower() == 'o' or c.lower() == 'u':
            word = word.replace(c, "")
    return word

if __name__ == "__main__":
    main()
