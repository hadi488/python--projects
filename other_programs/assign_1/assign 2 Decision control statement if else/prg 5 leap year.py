year = int(input("enter an year : "))
count = 0
if(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")