import random 
import os
def sum(a , b):
    return a + b 
print("Welcome to Blackjack Game.")
A, J, Q, K = 11, 10, 10, 10  #If total > 21  A = 1 
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, A, J, Q, K]
Computer_Cards, Player_Cards= [], []
Computer_Cards_sum, Player_Cards_sum = 0, 0 
start = input("Type 'y' or 'n' to get card: ")
if start == 'y':
    start = True
else:
    start = False
while start:
    A = 11
    if Player_Cards_sum < 17 or another_card == 'y':
        Player_Cards.append(random.choice(cards))
    if Computer_Cards_sum < 17:
        Computer_Cards.append(random.choice(cards))
    Player_Cards_sum = 0
    for i in Player_Cards:
        if i == A and Player_Cards_sum + i > 21:
            A = 1 
            Player_Cards_sum += A
        else:
            Player_Cards_sum += i
    Computer_Cards_sum = 0
    for i in Computer_Cards:
        if i == A and Computer_Cards_sum + i > 21:
            A = 1
            Computer_Cards_sum += A 
        else:
            Computer_Cards_sum += i 
    if Player_Cards_sum == 21:
        print("Congratulations, You win with BlackJack.")
        break
    if Player_Cards_sum > 21:
        print(f"Your cards: {Player_Cards}, score: {Player_Cards_sum}")
        print(f"Computer cards: {Computer_Cards}, score: {Computer_Cards_sum}")
        print("You Lose, Your cards sums over 21")
        break
    if Computer_Cards_sum > 21:
        print(f"Your cards: {Player_Cards}")
        print(f"Computer cards: {Computer_Cards}")
        print("You win, Computers cards sum over 21")
        break
    if Player_Cards_sum > 16:
        print(f"Your cards: {Player_Cards}, current score: {Player_Cards_sum}")
        print(f"Computer first card: {Computer_Cards[0]}")
        another_card = input("Type 'y' to get another card or Type 'n' to pass: ")
        if another_card == 'y':
            continue
        else:
            os.system("cls")
            print(f"Your final hand: {Player_Cards}, final score: {Player_Cards_sum}")
            print(f"Computer final hand: {Computer_Cards}, final score: {Computer_Cards_sum}")
            if Player_Cards_sum > Computer_Cards_sum:
                print("You Win :) ")
            elif Computer_Cards_sum > Player_Cards_sum:
                print("You Lose :( ")
            elif Computer_Cards_sum == Player_Cards_sum:
                print("Draw.")
            again = input("Do you want to play again?Type 'y' or 'n': ")
            if again == 'y':
                os.system("python .\Python_Workshop_2\Blackjack.py")
            else:
                start = False


    
