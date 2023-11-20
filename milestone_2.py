# import random

# word_list = ['apple', 'mango', 'strawberry', 'watermelon', 'banana']

# word = random.choice(word_list)
# print(word)


guess = input('Enter a single letter: ')
if len(guess) == 1 and guess.isalpha() == True:
    print(guess)
else:
    print('Oops')