import random
list = ["snake", "water", "gun"]
rand = random.randint(0, 2)
str1 = "snake"
computer = list[rand][0]
def gameWin(comp, you):
    if comp == you:
        print("It's a tie!")    
    elif (comp == 's' and you == 'w') or (comp == 'w' and you == 'g') or (comp == 'g' and you == 's'):
        print("You lose!")
    else:
        print("You win!")
print('Welcome to Snake Water Gun Game')  
user = input("Enter your choice (snake(s), water(w), gun(g)): ")
user = user.lower()
print(user)
gameWin(computer, user)
computer = list[rand]
print(f"Computer chose: {computer}")
