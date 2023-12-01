import random
from HangmanArt import stages
from HangmanArt import logo
from HangmanWords import word_list

chosen_word = random.choice(word_list)
letter_list = []
health = 6

print(logo)
end_of_game = False
for i in range(len(chosen_word)): #start 
    letter_list.append("_")
print(letter_list)
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if  letter == guess:
                letter_list[position] = letter
                print("Corrert guess.")
    if guess not in chosen_word:
        health -= 1    
        print(f"{guess} is not in word. You lost a life.")   
        print(stages[health])
      
        if health == 0:
            print("You lost")
            end_of_game = True
            print(chosen_word)
            
    print(letter_list)
    if "_" not in letter_list:
         end_of_game = True
         print("You Win.")