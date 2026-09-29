import random

def word_guessing_game():
    words = ['football', 'bat', 'laptop', 'chocolate', 'car', 'piano']
    secret_word = random.choice(words)
    attemps = 3
    print("the words are :",words)
    print("welcome to word guessing game")
    print("the word which is choose by computer you have to guess it")
    print("(hint):{len(secret_word)}")
    print("{attemps = attemps is 3}")

    while attemps > 0:
        guess = input("choose word").lower().strip()

        if guess == secret_word:
             print("congratulatiion! you won the game")
             break
        else:
             attemps = attemps-1 
             if attemps > 0:
                 print("try again")
             else:
                 print("game over")
                 print("you lose the game")
word_guessing_game()
