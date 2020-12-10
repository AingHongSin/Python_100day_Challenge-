import random

#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

Word = random.choice(word_list)
print(Word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
Guess_word = input("Enter a letter here: ").lower()
        

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for letter in Word:
    if Guess_word == letter:
        print("Right")
    else:
        print("Wrong")
