sub1 = int(input("enter sub 1 marks out of 100 : "))
sub2 = int(input("enter sub 2 marks out of 100 : "))
sub3 = int(input("enter sub 3 marks out of 100 : "))
sub4 = int(input("enter sub 4 marks out of 100 : "))
sub5 = int(input("enter sub 5 marks out of 100 : "))

obt = sub1 + sub2 + sub3 + sub4 + sub5
tot = 500
perc = (obt/tot) * 100
print("percentage is %f" %perc)
if perc >= 90:
    print("A grade")
elif perc >= 80:
    print("B grade")
elif perc >= 70:
    print("C grade")
elif perc >= 60:
    print("D grade")
elif perc >= 50:
    print("E grade")
else :
    print("F fail")