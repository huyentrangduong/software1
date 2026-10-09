from player import Player
from item import Item
from function import main_menu, score, explore, run, take, harvest


with open("Final_Submission_of_Project/intro.txt", "r") as file:
    intro = file.read()
    print(intro)
with open("Final_Submission_of_Project/instruction.txt", "r") as file:
    instruction = file.read()
    print(instruction)
with open("Final_Submission_of_Project/mission0.txt", "r") as file:
    mission0 = file.read()
with open("Final_Submission_of_Project/mission1.txt", "r") as file:
    mission1 = file.read()
with open("Final_Submission_of_Project/mission2.txt", "r") as file:
    mission2 = file.read()
with open("Final_Submission_of_Project/mission3.txt", "r") as file:
    mission3 = file.read()
with open("Final_Submission_of_Project/mission4.txt", "r") as file:
    mission4 = file.read()
with open("Final_Submission_of_Project/mission5.txt", "r") as file:
    mission5 = file.read()
with open("Final_Submission_of_Project/score.txt", "r") as file:
    saved_score = file.read()
with open("Final_Submission_of_Project/data.txt", "r") as file:
    saved_data = file.read()

import os
if os.path.exists("Final_Submission_of_Project/data.txt"):
    ans = input("Do you want to comtinue the game? (y/n): ")
    if ans.lower() == 'y':
        with open("Final_Submission_of_Project/data.txt", "r") as file:
            lines = file.readlines()
            player_name = lines[0].strip()
            player_location = lines[1]
            total = lines[2].strip()
            player = Player(player_name, player_location)
            print(f"\nWelcome back, {player_name}")
            print(f"This is your location: {player_location}")
            print(f"Your score is: {total}")
        choice = input("\n✅ Enter a command from the main menu:\n 1.explore\n 2.run\n 3.take\n 4.harvest\n 5.lopeta\n").strip()
    else:    
        print("Please input your information:")
        player_name = input("   - Name of gamer: ")
        player_location = input("   - Location: ")
        player = Player(player_name, player_location)
        item = Item("Water Bottle",100)
        player.collect_item(item)
        total = 0
        choice = main_menu()

total = 0
while choice != "lopeta" and choice != "5":
    if choice == "explore" or choice == "1":
        explore(player)
        print(mission0)
        print("Let's review your performance: ")
        choice = main_menu()

    elif choice == "run" or choice == "2":
        print(mission1)
        run(player)
        total= score(total)
        print(f"🔅 Congratulation! You completed the 1st mission. Your score is {total}.")
        print("Let's review your performance: ")
        choice = main_menu()

    elif choice == "take" or choice == "3":
        print(mission2)
        take(player)
        total= score(total)
        print(f"🔅 Congratulation! You completed the 2nd mission. Your score is {total}.")
        choice = main_menu()

    elif choice == "harvest" or choice == "4":
        print(mission3)
        harvest(player)
        total= score(total)
        print(f"🔅 Congratulation! You completed the 3rd mission. Your score is {total}.")
        print("Let's review your performance: ")
        print("\n🏁 Now you need to return to the starting point.")
        extra = input("Do you want to do extra mission? \n   - Yes\n   - No\n")
        if extra == "yes" or extra == "Yes" or extra == "y":
            print(mission4)
        else:
            print("You can go through the forest and walk to the starting point.")
        selection= input("\nNow is your choice, you can change your mind:\n   1.Walk 🌳\n   2.Boat 🛶\n")       
        if selection == "boat" or selection == "2":
            print(mission5)
            total= score(total)
            print(f"🎉 Congratulation! You completed the Save Forest adventure. Your score is {total}.")
            break
        else:  
            print("You follow your map and compass then reach the starting point.")
            print(f"🎉 Congratulation! You completed the Save Forest adventure. Your score is {total}.")
        break

with open("Final_Submission_of_Project/score.txt", "w") as file:
    file.write(f"🎉 Congratulation! You completed the mission. Your score is: {total}")
with open("Final_Submission_of_Project/data.txt", "w") as file:
    file.write(f"Player: {player_name}\nLocation: {player_location}\nScore: {total}\nChoices: {choice}")

print ("You stop the game")


