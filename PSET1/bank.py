# if the teller doesn't greet with hello, the customer gets $100
# if the teller greets with words that start with an "h", the customer gets $20

greeting = input("Greeting: ").strip().lower()

if greeting[0:5] == "hello":
    print("$0")
elif greeting[0:1] == "h":
    print("$20")
else:
    print("$100")

