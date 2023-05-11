import random

SCORE = []

def main():
    while True:
        num_input = input("This is a random number guessing game, pick what you want the numbers to go up to: ")
        while str(num_input.lower()) == 'quit':
            quit_ans = input("Are you sure you want to quit? Score won't be saved. ")
            if str(quit_ans.lower()) == 'yes':
                break
                break
            elif str(quit_ans.lower()) == 'no':
                print("No worries! Enjoy playing.")
                num_input = input("This is a random number guessing game, pick what you want the numbers to go up to: ")
                break
            else:
                print("Enter valid answer 'YES' or 'NO'")
        if num_input == 'quit':
            break
        y_n = input(f"Is {num_input} the number you want to use? ANSWER Y OR N ")
        if str(y_n.lower()) == "y":
            num_for_game = random.randrange(1, int(num_input))
            guess = input("Now guess what number the computer picked! ")
            if int(guess) == int(num_for_game):
                print("Congratulations! You guessed correct!")
                SCORE.append(1)
                print(f"Score is currently {sum(SCORE)}")
            else:
                print("Unfortunately, you got the number wrong. Try again!")
        elif str(y_n.lower()) == "n":
            print("No worries! Try to input the right number now.")

main()