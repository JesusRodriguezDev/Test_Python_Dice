import random
import time

playerPoints = 0
enemyPoints = 0


for i in range(10):
    playerRandomNum = random.randint(1, 6)
    enemyRandomNum = random.randint(1, 6)

    input("Press any key to roll the dice")
    print("You rolled a " + str(playerRandomNum))
    print("...Waiting on Enemy AI to roll")
    time.sleep(2)
    print("The enemy AI rolled a " + str(enemyRandomNum))
    print("")

    if playerRandomNum > enemyRandomNum:
        print("You win this round! You have earned a point")
        print("")
        playerPoints += 1
    elif playerRandomNum < enemyRandomNum:
        print("You lose this round! Enemy AI earned a point")
        print("")
        enemyPoints += 1
    else:
        print("Player and AI tied! No points earned")
        print("")

print("Player has " + str(playerPoints) + " points")
print("Enemy AI has " + str(enemyPoints) + " points")

if playerPoints > enemyPoints:
    print("You win!!!")
elif playerPoints < enemyPoints:
    print("You lose!!!")
else:
    print("Player and Enemy AI tied!!")

print("Game Over")
