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
i = sm
lcm = 1
while(i <= x * y):
    if i % sm == 0 and i % l == 0:
        lcm = i
        break
    i = i+1
print(f"lcm of {x} and {y} is {lcm} ")
