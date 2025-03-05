import random
"""
1 for snake
-1 for water
0 for gun
"""

computer = random.choice([-1,0,1])

yourstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ")

# Dictionary to change user input ('s', 'w', 'g') into numbers (1, -1, 0)
yourDict={"s":1,"w":-1,"g":0}
# Dictionary to change numbers (1, -1, 0) back into words (Snake, Water, Gun)
reverseDict={1:"Snake",-1:"Water",0:"Gun"}
# Convert the user's input into a number using the dictionary
you = yourDict[yourstr]

print(f"Your choise {reverseDict[you]}")
print(f"Computer choise {reverseDict[computer]}")

if (computer == you):
    print("Its a draw")
else:
    if(computer == -1 and you == 1):
        print("You win!")
    elif(computer == -1 and you == 0):
        print("You lose!")
    elif(computer == 1 and you == -1):
        print("You lose!")
    elif(computer == 1 and you == 0):
        print("You win!")
    elif(computer == 0 and you == -1):
        print("You win!")
    elif(computer == 0 and you == 1):
        print("You lose!")
    else:
        print("Something went worng!")
    
