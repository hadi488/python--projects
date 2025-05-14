import random
list = ["rock", "paper", "scissor"]
score = 0
tot_games = 0
lose_games = 0
tie_games = 0
def gameWin(comp, you):
    global tot_games
    global lose_games
    global tie_games
    tot_games += 1
    if comp == you:
        print("It's a tie!")    
        tie_games += 1
    elif (comp == 'r' and you == 's') or (comp == 'p' and you == 'r') or (comp == 's' and you == 'p'):
        print("You lose!")
        lose_games += 1
    else:
        print("You win!")
        global score
        score += 1
print('Welcome to rock paper scissor Game')  
print("rules of the game")
print("you will win if comp choose rock and you choose paper , or comp = paper and You = scissor , or comp = scissor and You = rock")
print("you will lose if comp choose rock and you choose scissor , or comp = paper and You = rock , or comp = scissor and You = paper")
print("it will tie if computer and you choose same")
while True:
    user = input("Enter your choice (Rock(R), paper(p), sciccor(s)) or q to quit: ")
    user = user[0].lower()
    if user == 'q':
        print(f"thanks for playing game you win {score} out of {tot_games} games and lose {lose_games} and  {tie_games} tie games")
        exit()
    elif(user == "r" or user == "p" or user == "s" ):
        rand = random.randint(0, 2)
        computer = list[rand][0]
        gameWin(computer, user)
        computer = list[rand]
        print(f"Computer chose: {computer}")
    else:
        print("invalid choice try again")
