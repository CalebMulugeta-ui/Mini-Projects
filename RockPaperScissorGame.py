import random

flag = True
while flag:
    try:
        userRound = int(input("Number for rounds: "))
        flag = False
    except ValueError:
        print("Not a number")
        continue

botsPoints = 0
userPoints = 0

while userRound > 0:
    choiceList = ['Rock', 'Paper',"Scissors"]
    botChoice = choiceList[random.randint(0,2)]

    flag = True
    flag2 = True
    while flag:
        try:
            while flag2:
                choice = int(input("Pick 0-Rock, 1-Paper, 2-Scissors: "))
                if choice < 0 or choice > 2:
                    print('Not a number between 0-2')
                    continue
                else:
                    flag2 = False
            flag = False
        except ValueError:
            print("Not a number between 0-2")
            continue


    userChoice = choiceList[choice]
    #ROCK VS SCISSORS
    if ((userChoice == 'Rock') and (botChoice == 'Scissors')):
        print(f"    Bot Choice: {botChoice}")
        print(f'    You won, +1 point\n')
        userPoints += 1
        userRound -= 1
        continue
    elif ((userChoice == 'Scissors') and (botChoice == 'Rock')):
        print(f"    Bot Choice: {botChoice}")
        print(f'    You lost, +0 point\n')
        botsPoints += 1
        userRound -= 1
        continue

    #PAPER VS ROCK
    elif ((userChoice == 'Paper') and (botChoice == 'Rock')):
        print(f"    Bot Choice: {botChoice}")
        print(f'    You won, +1 point\n')
        userPoints += 1
        userRound -= 1
        continue
    elif ((userChoice == 'Rock') and (botChoice == 'Paper')):
        print(f"    Bot Choice: {botChoice}")
        print(f'    You lost, +0 point\n')
        botsPoints += 1
        userRound -= 1
        continue

    #SCISSORS VS PAPER
    elif ((userChoice == 'Scissors') and (botChoice == 'Paper')):
        print(f"    Bot Choice: {botChoice}")
        print(f'    You won, +1 point\n')
        userPoints += 1
        userRound -= 1
        continue
    elif ((userChoice == 'Paper') and (botChoice == 'Scissors')):
        print(f"    Bot Choice: {botChoice}")
        print(f'    You won, +1 point\n')
        userPoints += 1
        userRound -= 1
        continue

    #Paper VS Paper
    elif ((userChoice == 'Paper')and (botChoice == 'Paper')):
        print(f"    Bot Choice: {botChoice}")
        print(f"    Tie\n")
        userRound -= 1

    #Rock vs Rock
    elif ((userChoice == 'Rock')and (botChoice == 'Rock')):
        print(f"    Bot Choice: {botChoice}")
        print(f"    Tie\n")
        userRound -= 1

    #Scissors Vs Scissors
    elif ((userChoice == 'Scissors')and (botChoice == 'Scissors')):
        print(f"    Bot Choice: {botChoice}")
        print(f"    Tie\n")
        userRound -= 1
print(f'    ------------')
print(f'    END OF GAME')
print(f'    ------------')
print(f"    Your Score: {userPoints} ")
print(f"    Bot Score: {botsPoints}")
if botsPoints > userPoints:
    print(f'    BOT WINS!')
elif userPoints > botsPoints:
    print(f'    YOU WIN!')
else:
    print(f'    TIE')
