import random
questions =  ['1. What is the capital of Australia?',
              '2. What is the largest planet in our solar system?',
              '3. Who wrote "Romeo and Juliet"?',
              '4. What is the chemical symbol for gold?',
              '5. What is the largest mammal in the world?',
              '6. Who painted the Mona Lisa?',
              '7. What is the smallest country in the world?',
              '8. What is the longest river in the world?',
              '9. Who discovered penicillin?',
              '10. What is the hardest natural substance on Earth?',]

answers = ['C. Canberra',
           'C. Jupiter',
           'B. William Shakespeare',
           'B. Au',
           'B. Blue Whale',
           'C. Leonardo da Vinci',
           'B. Vatican City',
           'B. Nile River',
           'B. Alexander Fleming',
           'A. Diamond',]
              
options = [['A. Sydney', 'B. Melbourne', 'C. Canberra', 'D. Brisbane'],
           ['A. Earth', 'B. Saturn', 'C. Jupiter', 'D. Mars'],
           ['A. Charles Dickens', 'B. William Shakespeare', 'C. Mark Twain', 'D. Jane Austen'],
           ['A. Ag', 'B. Au', 'C. Pb', 'D. Fe'],
           ['A. Elephant', 'B. Blue Whale', 'C. Giraffe', 'D. Hippopotamus'],
           ['A. Vincent van Gogh', 'B. Pablo Picasso', 'C. Leonardo da Vinci', 'D. Claude Monet'],
           ['A. Monaco', 'B. Vatican City', 'C. Nauru', 'D. San Marino'],
           ['A. Amazon River', 'B. Nile River', 'C. Yangtze River', 'D. Mississippi River'],
           ['A. Louis Pasteur', 'B. Alexander Fleming', 'C. Marie Curie', 'D. Thomas Edison'],
           ['A. Diamond', 'B. Gold', 'C. Sapphire', 'D. Ruby'],]

useranswer = None
firstanswer = None
finalanswer = None
score = 10
values  = ["A", "B", "C", "D"]
random_numbers = []

def get_random_number(start, end):
    rand = random.randint(start, end)
    while rand in random_numbers:
        rand = random.randint(start, end)
    random_numbers.append(rand)
    return rand
    
def display_question(question, options):
    print(question)
    for option in options:
        print(option)
    
def check_answer(useranswer, correctanswer):
    correctanswer = correctanswer.upper()
    if useranswer == correctanswer:
        return True
    else:
        calculate_score()
        return False
    
def calculate_score():
    global score
    score = score - 1
    return

def show_result():
    print(score)
    if  useranswer == 'E':
        print("You have exited the game.")
        print("unfortunately! You have lost all the money.")
    elif not useranswer == 'E' :
        print("You have completed the quiz.")
        print(f"You correct {score} questions.")
        print(f"congratulations! you won {score} crore Rs.")
    elif score == 0:
        print("You have completed the quiz.")
        print(f"You correct {score} questions.")
        print("unfortunately! You have lost all the money.")
        
print("Welcome to the Quiz Game!")
print("You will be asked 10 questions. Choose the correct option (A, B, C, or D) for each question.")
print("You can exit the game at any time by typing 'exit'. if you exit in between the game you will lose all money even if yoy correct all the questions before.")
print("total amount is 10 crore Rs so for each one wrong answer you will lose 1 Crore.")
print("you can skip question but you will lose 1 crore Rs for that question.")
print("Let's get started!")
input("Press Enter to start the Game...")
for i in range(len(questions)):
    rand = get_random_number(0,9)
    display_question(questions[rand], options[rand])
    print("Your answer: ", end='')
    firstanswer = input('choose one correct option in the given options A ,B, C ,D or "e" to quit the game or "s" the question: ')
    firstanswer = firstanswer.upper()
    finalanswer = input('Are you sure for the answer if yes then type "y" or want to change the answer if yes then choose in the given options A ,B, C ,D or type "e" to quit the game: or type "s" to skip the question: ')
    finalanswer = finalanswer.upper()
    if finalanswer == 'Y':
        useranswer = firstanswer
    elif finalanswer == 'S':
        useranswer = finalanswer
        print("You skipped the question. you lost 1 crore Rs.")
        calculate_score()
        continue
    elif finalanswer == 'E':
        useranswer = finalanswer
        print("Thanks for playing! you have exited the game. and you have lost all the money.")
        score = 0
        break
    else:
        useranswer = finalanswer
    
    useranswer = useranswer.upper()
    userans = options[rand][values.index(useranswer)]
    print("Your answer is:", userans)
    print("Correct answer is:", answers[rand])
    print("--------------------------------------------------")
    check = check_answer(useranswer, answers[rand][0])
    if check:
        print("Correct!")
    else:
        print("Wrong! The correct answer is:", answers[rand])
    print("--------------------------------------------------")
    
print("--------------------------------------------------")
show_result()






