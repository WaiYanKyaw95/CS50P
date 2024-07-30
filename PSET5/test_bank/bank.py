# if the teller doesn't greet with hello, the customer gets $100
# if the teller greets with words that start with an "h", the customer gets $20
# if the teller greets with hello, the customer will not get anything
def main():
    greeting_text = input("Greeting: ")
    print(f"${value(greeting_text)}")

# ensure the case-insensitive input from users
# first greet with hello, return 0
# greet with word starting with an h, return 20
# greet with word other than h or hello, return 100
def value(greeting):
    greeting = greeting.strip().lower()
    if greeting[0:5] == "hello":
        x = 0
    elif greeting[0:1] == "h":
        x = 20
    else:
        x = 100
    return x

if __name__ == "__main__":
    main()
