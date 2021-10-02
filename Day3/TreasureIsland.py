"""
Alexander Clarke
Day 3 project for 100 Days of Code
"""

print( '''       _                                     _     _                 _ 
      | |                                   (_)   | |               | |
      | |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
      | __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
      | |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
       \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 ''')
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome Treasure Island, where each decision will lead you one step closer to treasure, or your demise.")
choice1 = input("You start your journey at a crossroads, where would you like to go? Type \"left\" or \"right\"\n").lower()

if (choice1 == "left"):
    choice2 = input("You arrive at a lake, do you wait for a boat or swim across? Type \"boat\" to wait or \"swim\" to swim across.\n").lower()
    if (choice2 == "boat"):
        choice3 = input("You made it safely across the lake. There is a house with three doors, one \"red\", one \"yellow\", and one \"blue\".\n").lower()
        if (choice3 == "red"):
            print("You enter a room that erupts into flames. Game Over")
        elif (choice3 == "yellow"):
            print("You enter a room with a large chest in the center. You open it up to find treasure. You Won!")
        elif (choice3 == "blue"):
            print("You enter a dark room and smell death. A monster grabs you. Game Over")
    else:
        print("You were attacked by a lake serpant and die. Game Over")
else:
    print("You fell into a hole and died. Game Over")
