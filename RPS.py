import random
print("Lets play Rock paper Scissors")
print("two players secretly pick one of “rock,” “paper,” or “scissors.”\nBoth players reveal their selection to the other player at once; the winner is chosen based on what the selections are.\n Rock beats scissors (by crushing them); \n scissors beats paper (by cutting it); and paper beats rock (by covering it).\n If both players select the same one, it is a tie.\n\n")

print ("Enter the selection amoung rock , paper and scissor(enter in lower case with no spaces)\n")
player = input()
options = ["rock","paper","scissor"]
computer = random.choice(options)

print(" player =",player,"\n computer = ",computer,"\n")
while (player == computer):
    print("it's a tie, lets rematch")
    print ("Enter the selection amoung rock , paper and scissor(enter in lower case with no spaces)\n")
    player = input()
    options = ["rock","paper","scissor"]
    computer = random.choice(options)
    
if ((player == "rock" and computer == "scissor" ) or (player == "scissor" and computer == "paper") or (player == "paper" and computer == "rock" ) ):
    print("Player wins")
else:
    print("Computer wins")


