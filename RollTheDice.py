import random

def roll() :
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True :
    player = input("Enter the number of players (2 - 4): ")
    
    if player.isdigit() :
        player = int(player)
        if 2 <= player <= 4 :
            break
        else :
            print("Only 2 - 4 players are allowed")
    else :
        print("Invalid input, try again")

max_score = 10
player_score = [0 for i in range(player)]

while max(player_score) < max_score :

    for player_id in range(player) :
        print("\nPlayer number",player_id + 1 ,"turn started...\n")
        print("Your total score is: ",player_score[player_id],"\n")
        current_score = 0

        while True :
            should_roll = input("Would you like to roll (y)")
            if should_roll.lower() != "y" :
                break

            val = roll() 
            if val == 1 :
                print("You rolled a 1, you lose all your points")
                current_score = 0
                break
            else :
                current_score += val
                print("You rolled a: ",val)
            print("Your Score is: ",current_score)

        player_score[player_id] += current_score 
        print("Your total score is: ",player_score[player_id])

max_score = max(player_score)
winning_id = player_score.index(max_score)
print("Player number",winning_id + 1,"won the game with the score of: ",max_score)