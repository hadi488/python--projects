# month = int(input("enter month in numeric format : "))
# if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
#     print("this month has 31 days")
# elif (month == 2):
#     print("this month has 28 days if leap year then it has 29 days")
# else:
#     print("this month has 30 days")
#
#

month = int(input("Enter month in numeric format (1-12): "))
if month < 1 or month > 12:
    print("Invalid month! Please enter a number between 1 and 12.")
elif month in [4,6,9,11]:
    print("This month has 30 days.")
elif month == 2:
    print("This month has 28 days. If it's a leap year, it has 29 days.")
else:
    print("This month has 31 days.")
