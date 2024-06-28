months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    month, day, year = formatMonth()
    print(f"{year}-{month:02}-{day:02}")

def formatMonth():
    while True:
        date = input("Date: ")  #   prompt for user input
        try:
            if "/" in date:     #   if it is in mm/dd/yyyy format
                mm, dd, yyyy = date.strip().split("/")
            elif "," in date:   #   if it is in mmmm dd, yyyy format
                mm, dd, yyyy = date.strip().replace(",", "").split()    #   remove the comma and split the date into a list
                mm = months.index(mm) + 1       #   use index method to retrieve the index of the month from the months list and add 1
            if int(mm) > 12 or int(dd) > 31:    #   check if the month and daysubmit50 cs50/problems/2022/python/outdated are correct
                raise ValueError
            return int(mm), int(dd), int(yyyy)  #   return the values
        except (ValueError, TypeError, UnboundLocalError, KeyError):
            pass

main()
