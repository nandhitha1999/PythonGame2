#include <stdio.h>

import random 
from collections import Counter 

def select(): 
    print('HANGMAN GAME :-) Guess the word!')
    choice = random.randrange(1,4)
    if (choice==1):
        print('HINT: The word is a fruit')
        return fruits
    elif (choice==2):
        print('HINT: The word is a vegetable')
        return vegetables
    else:
        print('HINT: The word is a ')
        return colours
    
    
fruits = '''apple orange banana pomagranate mango avacado strawberry kiwi grape pineapple blueberry 
apricot lemon pear coconut fig watermelon cherry papaya plum berry peach lychee muskmelon raspberry'''

vegetables = '''tomato carrot brinjal potato beans pumpkin bittergourd chilli garlic mushroom cauliflower
brocolli corn eggplant capsicum onion lettuce beetroot chickpea cabbage'''

colours = '''red yellow pink blue orange indigo green violet purple white black brown grey maroon '''
  
fruits = fruits.split(' ') 
vegetables = vegetables.split(' ')
colours = colours.split(' ')

word = random.choice(select())          
  
if __name__ == '__main__':
    
    for i in word: 
        print('_', end = ' ')         
    print() 
  
    play = True
    guessLetter = ''                 
    chances = len(word) + 2
    correct = 0
    flag = 0
    
    try: 
        while (chances != 0) and flag == 0:   
            print() 
            chances -= 1
  
            try: 
                guess = str(input('>> Enter a letter to guess: ')) 
            except: 
                print('Enter only a letter!') 
                continue
            if not guess.isalpha(): 
                print('Enter only a LETTER') 
                continue
            elif len(guess) > 1: 
                print('Enter only a SINGLE letter') 
                continue
            elif guess in guessLetter: 
                print('You have already guessed that letter') 
                continue
            elif guess in word: 
                count = word.count(guess) #k stores the number of times the guessed letter occurs in the word
                print('Correct guess!')
                for _ in range(count):     
                    guessLetter += guess # The guess letter is added as many times as it occurs
            else:
                print('Wrong guess!')
  
            for char in word: 
                if char in guessLetter and (Counter(guessLetter) != Counter(word)): 
                    print(char, end = ' ') 
                    correct += 1
                elif (Counter(guessLetter) == Counter(word)):
                    print("The word is : ", end=' ') 
                    print(word) 
                    flag = 1
                    print('\nWow, You found the word! YOU WIN THE GAME!\nYour Hangman is alive') 
                    break 
                    break 
                else: 
                    print('_', end = ' ')
        if chances <= 0 and (Counter(guessLetter) != Counter(word)): 
            print() 
            print('\nWrong guess! Try again..The word was : {}'.format(word)) 
            print('YOU LOST! Your Hangman is dead!') 
  
    except KeyboardInterrupt: 
        print() 
        print('Bye! Try again.') 
        exit()
