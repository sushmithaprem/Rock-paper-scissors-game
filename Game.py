import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("=" * 40)
print("     🎮 ROCK PAPER SCISSORS 🎮")
print("=" * 40)

while True:
    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = input("\nYour choice: ").lower()

    # Check valid input
    if user_choice not in choices:
        print("❌ Invalid choice! Please choose rock, paper, or scissors.")
        continue

    # Computer choice
    computer_choice = random.choice(choices)

    print("\n------------------------------")
    print("You      :", user_choice)
    print("Computer :", computer_choice)
    print("------------------------------")

    # Game logic
    if user_choice == computer_choice:
        print("🤝 It's a TIE!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or
        (user_choice == "scissors" and computer_choice == "paper")
        or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("🎉 You WIN!")
        user_score += 1

    else:
        print("😢 You LOSE!")
        computer_score += 1

    # Score
    print("\n📊 SCORE")
    print("You      :", user_score)
    print("Computer :", computer_score)

    # Play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("\n" + "=" * 40)
print("           GAME OVER")
print("=" * 40)

print("Final Score")
print("You      :", user_score)
print("Computer :", computer_score)

if user_score > computer_score:
    print("🏆 Congratulations! You are the champion!")
elif computer_score > user_score:
    print("🤖 Computer wins the game!")
else:
    print("🤝 The game ended in a draw!")

print("=" * 40)