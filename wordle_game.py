import random 

def give_instructions():
    print('''\nWordle is a word guessing game.
    You have 5 attempts
    (C) means the letter is in the word and is in the correct position.
    (WP) means the letter is in the word but not in the correct position.
    (NT) means the letter is not in the word itself at all.

    Best of Luck!''')

words = ["this", "five", "help", "lake", "pink", "cats"]
hidden_word = random.choice(words)
attempts = 5

def check_word(guess, hidden_word):
    if hidden_word == guess:
        print("Congrats!! You did it.")
        return True
    else:
        result = ""
        for i, j in zip(guess, hidden_word):
            if i == j:
                result = result + "(C)"
            elif i in hidden_word:
                result = result + "(WP)"
            else:
                result = result + "(NT)"
        print(result)
        return False

def main():
    attempts = 5
    give_instructions()
    while attempts > 0:
        guess = input("Enter four-letter word: ")
        if check_word(guess, hidden_word):
            break
        else:
            attempts -= 1
            print(f"You have {attempts} attempts left.")

if __name__ == "__main__":
    main()