# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘
import random


dice_art = {
    1: ("┌──────────┐",
        "│          │",
        "│     ●    │" ,
        "│          │",
        "└──────────┘" ),
    2: ("┌──────────┐",
        "│  ●       │",
        "│          │" ,
        "│        ● │",
        "└──────────┘" ),
    3: ("┌──────────┐",
        "│  ●       │",
        "│     ●    │" ,
        "│        ● │",
        "└──────────┘" ),
    4: ("┌──────────┐",
        "│  ●     ● │",
        "│          │" ,
        "│  ●     ● │",
        "└──────────┘" ),
    5: ("┌──────────┐",
        "│  ●     ● │",
        "│     ●    │" ,
        "│  ●     ● │",
        "└──────────┘" ),
    6: ("┌──────────┐",
        "│  ●     ● │",
        "│  ●     ● │" ,
        "│  ●     ● │",
        "└──────────┘" ),
}

dice = []
total = 0

no_of_dice = int(input("how nany dice"))

for die in range(1,no_of_dice+1):
    dice.append(random.randint(1,6))
    
for el in dice:
    total += el
    
# for a in range(no_of_dice):
#     for line in dice_art.get(dice[a]):
#         print(line)
#     print()

for line in range(5):
    for d in dice:
        print(dice_art[d][line], end= " ")
    print()
        
    
print(f"total = {total}")
# print(dice)
