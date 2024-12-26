import random

attempts = 10

def read_words_from_file(file_name):
    with open(file_name, "r") as file:
        words = file.read().splitlines()
    return words

words = read_words_from_file("wordBank.txt")

word = random.choice(words)

guessedWord = ['_'] * len(word)


while (attempts > 0):
    print("\nCurrent Word: " + " ".join(guessedWord))
    guess = input("Guess a letter: ")
    if guess in word: 
        for i in range(len(word)):
            if word[i] == guess: 
                guessedWord[i] = guess
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong:(  " + str(attempts) + " Attempts left.")
    if '_' not in guessedWord: 
        print('\nYou guessed the word, Yay!')
        break
if attempts == 0: 
    print("..Ran out of attempts:(  The word was: " + word)

