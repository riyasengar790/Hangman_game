import pyfiglet
from hangman_words import word_list
import random

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives =6

s="Welcome to hangman game"
print(pyfiglet.figlet_format(s))
#Create blanks
display = []

for _ in range (word_length):
    display+='_'
print(display)  

end_of_game = False
while not end_of_game:
    
    guess = input("enter a alphabet").lower()
    
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")


    #Check guessed letter
    for position  in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display) 

    
    if guess not in display:
        #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives-=1
        if lives==0:
            end_of_game=True   
            g="you lose"
            print(pyfiglet.figlet_format(g)) 
     
    #Join all the elements in the list and turn it into a String. 
    print(f"{' '.join(display)}") 

    #Check if user has got all letters.       
    if '_' not in display:
        end_of_game = True
        w="you win"
        print(w)

  #Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    print(stages[lives])   
