#Task #1:

year = int(input("Enter a year: "))

if year % 4 == 0 and year % 100 != 0:
    print("That is a leap year")
elif year % 400 == 0:
    print("That is a leap year")
else:
    print("That's not a leap year")
