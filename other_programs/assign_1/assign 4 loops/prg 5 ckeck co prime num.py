x = input("enter first number: ")
y = input("enter sec number: ")

x = int(x)
y = int(y)
sm = x
l = y
if x < y:
    sm = x
    l = y
else:
    sm = y
    l = x
print("greater = ", l, "small = ",sm)
i = 2
while(i <= sm):
    if sm % i == 0 and l % i == 0:
        print(f"{x} and {y} are not co prime ")
        break
    i = i+1
else:
    print(f"{x} and {y} are co prime ")
