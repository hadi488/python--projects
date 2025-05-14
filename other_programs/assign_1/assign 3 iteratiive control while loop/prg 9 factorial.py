
i = 1
n = int(input("enter a number: "))
if(n < 0):
    print("negative number factorial not valid")
else:
    fact = 1
    while (i <= n):
        fact *= i
        i += 1
    print(f"factorial of {n} is {fact}")

