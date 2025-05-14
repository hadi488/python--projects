
i = 1
n = int(input("enter a number: "))
prod = 1
while(i <= n):
    prod *= i*2-1
    i += 1
print(f"product of first {n} odd natural number is {prod}")
