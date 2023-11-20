
# while True:
#     guess = input("guess a letter: ")
#     if guess.isalpha():
#        if guess in secret_word:
#           print(f'Good guess! {guess} is in the word')
#        else:
#           print(f'Sorry, {guess} is not in the word. Try again.')
           
#     else: 
#         print("Invalid Letter. Please, enter a single alphabetical character.")
     

def check_guess(guess):
    guess_lower = guess.lower()
    if guess_lower in secret_word:
        print(f'Good guess! {guess_lower} is in the word')
    else:
        print(f'Sorry, {guess_lower} is not in the word. Try again.')



def ask_for_input():
    while True:
        guess = input("guess a letter: ")
        if guess.isalpha():
            break
        else: 
            print("Invalid Letter. Please, enter a single alphabetical character.")
        
    check_guess(guess)

secret_word = 'apple'
ask_for_input()