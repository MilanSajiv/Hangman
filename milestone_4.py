import random

class Hangman:
    def __init__(self, world_list, num_lives = 5) -> None:
        self.word_list = world_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word = self.pick_random_word()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
    
    def pick_random_word(self):
        return random.choice(self.word_list)

    def check_guess(self, guess):
        guess_lower = guess.lower()

        if guess_lower in self.word:
            print(f'Good guess! {guess_lower} is in the word.')
            for i in range(len(self.word)):
                if self.word[i] == guess_lower:
                    self.word_guessed[i] = guess_lower
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess_lower} is not in the word.')
            print(f'You have {self.num_lives} lives left.')
    
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            guess_lower = guess.lower()

            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess_lower in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess_lower)
                self.list_of_guesses.append(guess_lower)
                break     
