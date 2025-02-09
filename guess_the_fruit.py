import random
import time

def guess_the_fruit():
    easy_fruits = ["pear", "banana", "grape", "kiwi", "mango"]
    medium_fruits = ["cherry", "orange", "papaya", "peach", "guava"]
    hard_fruits = ["pomegranate", "blueberry", "blackberry", "watermelon", "cranberry"]

    print("Welcome to the 'Guess the Fruit' game!")
    print("I have selected a fruit. You need to guess it one letter at a time.")
    
    # Select a difficulty level
    difficulty = input("Choose a difficulty level (Easy, Medium, Hard): ").strip().lower()
    if difficulty == "medium":
        fruits = medium_fruits
        max_attempts = 10
    elif difficulty == "hard":
        fruits = hard_fruits
        # Set max attempts based on the length of the selected fruit
        selected_fruit = random.choice(fruits)
        max_attempts = len(selected_fruit)
    else: 
        fruits = easy_fruits
        max_attempts = float('inf')

    # Randomly select a fruit from the chosen list
    if difficulty != "hard":
        selected_fruit = random.choice(fruits)
    
    hidden_fruit = ["_"] * len(selected_fruit)
    print(f"You have {max_attempts if max_attempts != float('inf') else 'unlimited'} attempts to guess the fruit. Good luck!")
    
    # Keep track of attempts and guessed letters
    attempts = 0
    guessed_letters = set()
    start_time = time.time()  # Start the timer
    
    while attempts < max_attempts:
        # Display the current state of the hidden word
        print("\nCurrent word:", " ".join(hidden_fruit))
        print("Guessed letters:", ", ".join(sorted(guessed_letters)) if guessed_letters else "None")
        print(f"Attempts remaining: {max_attempts - attempts if max_attempts != float('inf') else 'unlimited'}")
        
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        attempts += 1
        if guess in guessed_letters:
            print("You already guessed that letter! Try again.")
            continue
        guessed_letters.add(guess)
        
        if guess in selected_fruit:
            print(f"Good guess! The letter '{guess}' is in the word.")
            for i, letter in enumerate(selected_fruit):
                if letter == guess:
                    hidden_fruit[i] = guess
        else:
            print(f"Sorry, the letter '{guess}' is not in the word.")
        
        if "_" not in hidden_fruit:
            end_time = time.time()  # Stop the timer
            print("\nCongratulations! You guessed the fruit:", selected_fruit.upper())
            print(f"It took you {attempts} attempts and {end_time - start_time:.2f} seconds to guess the word!")
            break
    else:
        print("\nGame Over! You've run out of attempts.")
        print(f"The fruit was: {selected_fruit.upper()}")

    # Calculate extra attempts used
    unique_letters_in_word = len(set(selected_fruit))  # Count unique letters in the fruit
    extra_attempts = attempts - unique_letters_in_word  # Subtract unique letters from total attempts
    if extra_attempts > 0:
        print(f"\nYou used {extra_attempts} extra attempt(s) beyond the unique letters in the fruit.")

if __name__ == "__main__":
    guess_the_fruit()
