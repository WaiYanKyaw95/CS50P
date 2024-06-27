def main():
    # Input from users
    t = input("What time is it? ").strip().lower()
    # invoking the function convert with input argument which will return h + m in decimal
    currentTime = convert(t)
    # if statement but this could also be a function
    if 7.0 <= currentTime <= 8.0:
        print("breakfast time")
    elif 12.0 <= currentTime <= 13.0:
        print("lunch time")
    elif 18.0 <= currentTime <= 19.0:
        print("dinner time")
    # print()

def convert(time):
    # retrieve the hour and minute which is in hh:mm format
    h, m = time.split(":")
    h, m = int(h), int(m)/60
    return h + m

# invoke the main function
if __name__ == "__main__":
    main()
