p_amout = float(input("enter priniple amount to be given: "))
year = int(input("enter time : first enter years: "))
month = int(input("now enter months: "))
rate = float(input("enter rate of interest in percentage: "))
time = ((year*12) + month)/12
print(time)
Si = p_amout * time * (rate/100)
print("simple interest is : ", Si)
print("Total amount to be return  : ", Si + p_amout)
