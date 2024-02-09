import HigherLoverArt
from HigherLoverData import data
import random
import os
def random_account():
    return random.choice(data)
againstB = random_account()
def fallower_number():
    print(f"{compareA['name']}'s fallower number is: {A_Fallowers}")
    print(f"{againstB['name']}'s fallower number is: {B_Fallowers}")
def correct_answer():
    global compareA
    if A_Fallowers > B_Fallowers:
        compareA = compareA
    else:
        compareA = againstB

while True: 
    compareA = random_account()
    score = 0
    while True:
        againstB = random_account()
        print(HigherLoverArt.logo)
        print(compareA["name"], compareA["description"], compareA["country"], sep= ", ")
        print(HigherLoverArt.vs)
        print(againstB["name"], againstB["description"], againstB["country"], sep= ", ")
        while True:
            chosen = input("What is your chose?'A' or 'B': ").upper()
            if chosen == 'A' or chosen == 'B':
                break
            else:
                print("Undefined value, Try Again")
        A_Fallowers = compareA['follower_count']
        B_Fallowers = againstB['follower_count']
        if chosen == "A" and B_Fallowers > A_Fallowers:
            print("Wrong Answer")
            fallower_number()
            break
        elif chosen == "B" and A_Fallowers > B_Fallowers:
            print("Wrong Answer")
            fallower_number()
            break        
        elif A_Fallowers == B_Fallowers:
            print("Draw Fallower")
            fallower_number()
            correct_answer()
            continue
        score += 1
        print("Correct Answer!")
        fallower_number()
        print(f"Your score: {score}")
        correct_answer()
    again = input("Do you want to play again? 'y' or 'n': ").lower()
    if again == "y":
        os.system("cls")
        continue
    else:
        break