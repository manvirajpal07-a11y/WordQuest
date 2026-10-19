## WordQuest




import random

## list of words
words=["apple","banana","mango","orange","kiwi","grapes","guava","watermelon","strawberry","pineapple","avocado","litchi"]




##function to get a random word
def get_random_word():
    return random.choice(words)




##function to display the correct progress of the word
def display_word_progress(word,guessed_letters):
    display = [letter if letter in guessed_letters else "_" for letter in word]
    print("Word: " + " ".join(display))
    
    
    
##function to get valid user guess
def get_user_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if len (guess)!=1 or not guess.isalpha():
            print("Please enter a single letter")
        elif guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            return guess


## Main fuction to play the game
def play_WordQuest():
    word = get_random_word()   # Randomly select a word
    guessed_letters = []       # List to store the guessed letters
    wrong_guesses = 0          # Counter for wrong guesses
    max_wrong_guesses = 6      # Maximum allowed wrong guesses
    
    print("Welcome to WordQuest !")
    
    while wrong_guesses < max_wrong_guesses:
        display_word_progress(word, guessed_letters)
        guess = get_user_guess(guessed_letters)
        guessed_letters.append(guess)
        
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses+=1
            print(f"Wrong guess! You have {max_wrong_guesses - wrong_guesses} attempts left.")
            
            
            
            ##Check if the player has guessed all the letters
        if all(letter in guessed_letters for letter in word):
           print(f"Congratulations! You have guessed the word: '{word}'")
           break
    else:
        print(f"Game over! The word was '{word}'")
                
                
## Run the game
play_WordQuest()
            
            
            
            
            
            

            
            
            
            
            
            
            
            
            
            
            
    