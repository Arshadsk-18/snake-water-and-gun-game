import random

'''
Snake Water Gun Game
Rules:
1 -> Snake
-1 -> Water
0 -> Gun
'''

# Mapping choices
userDict = {"S": 1, "W": -1, "G": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Scoreboard
user_score = 0
computer_score = 0
draws = 0

print("Welcome to Snake-Water-Gun Game!")
print("Enter 'S' for Snake, 'W' for Water, 'G' for Gun, or 'Q' to quit.\n")

while True:
    # Take user input
    userstr = input("Your choice (S/W/G/Q): ").upper()
    
    if userstr == "Q":  # Quit condition
        print("\nGame Over!")
        print(f"Final Score -> You: {user_score}, Computer: {computer_score}, Draws: {draws}")
        break

    if userstr not in userDict:  # Invalid input
        print("Invalid choice! Please enter S, W, G, or Q.")
        continue

    user = userDict[userstr]
    computer = random.choice([-1, 0, 1])  # Computer random choice

    # Show choices
    print(f"\nYou chose: {reverseDict[user]}")
    print(f"Computer chose: {reverseDict[computer]}")

    # Decide winner
    if computer == user:
        print("It's a Draw!\n")
        draws += 1
    else:
        if (computer == -1 and user == 1):
            print("🎉 You Win!\n")
            user_score += 1
        elif (computer == -1 and user == 0):
            print("😢 You Lose!\n")
            computer_score += 1
        elif (computer == 1 and user == -1):
            print("😢 You Lose!\n")
            computer_score += 1
        elif (computer == 1 and user == 0):
            print("🎉 You Win!\n")
            user_score += 1
        elif (computer == 0 and user == -1):
            print("😢 You Lose!\n")
            computer_score += 1
        elif (computer == 0 and user == 1):
            print("😢 You Lose!\n")
            computer_score += 1
        else:
            print("⚠️ Something went wrong!!")
