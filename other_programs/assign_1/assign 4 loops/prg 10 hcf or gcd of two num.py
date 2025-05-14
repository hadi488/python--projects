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
hcf = 1
while(i <= sm):
    if sm % i == 0 and l % i == 0:
        hcf = i
    i = i+1
print(f"Hcf of {x} and {y} is {hcf} ")
