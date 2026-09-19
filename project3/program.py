print("Please input your information:")
player_name = input("- Name of gamer: ")
player_age = int(input("- Age of gamer: "))
total = 0
bag = []
print ("======================================================================")

if player_age < 6:
    print("You are a minor. The game is shutting down.")

else:
    print("\nHello! " + player_name)
    print("Welcome to save Forest ❤️")
    print("Your mission is to protect the forest and help the environment.")

    print("\nYou need to complete three environmental missions:")
    print("- Mission 1: Water the tree 🌳")
    print("- Mission 2: Collect plastic waste ♻️")
    print("- Mission 3: Harvest the crops 🌾")

    print("\nTotal points that you can earn after completation all missons")
    print("- Each mission gives you 10 points.")
    print("- You can earn another 10 points by returning by boat.")
    print("-> The maximum score is 40 points.")
    print ("======================================================================")
    main_menu = input("\n✅ Enter a command from the main menu:\n 1.explore\n 2.run\n 3.take\n 4.harvest\n 5.lopeta\n")

    while main_menu != "lopeta":
        if main_menu == "explore" or main_menu == "1":
            print ("======================================================================")
            print("👍 Great! Let's start the adventure.")
            print(f"{player_name}, you are standing at the entrance of a beautiful forest")
            print("Before starting your journey, you receive an adventure bag.")
            
            def inventory (items):
                for item in items:
                    print(f" - {item}")
                return items

            bag.insert(3,"Water Bottom 🍶")
            bag.append("Map") 
            bag.append("Compass 🧭")
            inventory (bag)


            print("Now, open the bag and look at your map.")
            print("There is a big tree not far from here.")
            print("You have to RUN to the big tree for 1st mission.")
            print ("======================================================================")
            main_menu = input("\n✅ Enter a command from the main menu:\n1.explore\n2.run\n3.take\n4.harvest\n5.lopeta\n")


        elif main_menu == "run" or main_menu == "2":
            print ("======================================================================")
            print(f"👉 You are standing under the tree. Now, find the 1st mission .")
            print("🌳 MISSION 1")
            print("The tree is very dry.")
            print("It needs water.")
            print("Check the items in your bag.")
            print("\n💧 You use your water to water the tree.")
            print("The tree looks healthy again! 🌳")
            print("\nCheck the items in your bag:")
            print("Water Bottom 🍶 is no longer in the bag.")

            bag.remove("Water Bottom 🍶")
            inventory (bag)

            
            def score (total):
                total = total + 10
                return total

            total= score (total)
            print(f"🔅 Congratulation! You completed the 1st mission. Your score is {total}.")
            print ("======================================================================")
            main_menu = input("\n✅ Enter a command from the main menu:\n1.explore\n2.run\n3.take\n4.harvest\n5.lopeta\n")

        elif main_menu == "take" or main_menu == "3":
            print ("======================================================================")
            print("\n🌳 MISSION 2")
            print("You find a plastic bottle. Then take it and put it into your bag.")
            print("Goodjob! you contribute to clean the enviroment")
            print("\nCheck the items in your bag")

            bag.append("Plastic Bottle ♻️")  
            inventory (bag)

            total= score (total)
            print(f"🔅 Congratulation! You completed the 2nd mission. Your score is {total}.")
            print ("======================================================================")
            main_menu = input("\n✅ Enter a command from the main menu:\n1.explore\n2.run\n3.take\n4.harvest\n5.lopeta\n")

        elif main_menu == "harvest" or main_menu == "4":
            print ("======================================================================")
            print("\n🌳 MISSION 3")
            print("you harvest the crops. Then take it and put it into your bag.")
            print("\nCheck the items in your bag")

            bag.append("crops")   
            inventory (bag)
 
            total= score (total)
            print(f"🔅 Congratulation! You completed the 3rd mission. Your score is {total}.")
            print("\n🏠 Now you need to return to the starting point.")
            extra = input("Do you want to do extra mission? \n- Yes\n- No\n")
            if extra == "yes" or extra == "Yes" or extra == "y":
                print("\n🌳 EXTRA MISSION")
                print("\nThere are two different routes:")
                print("1. Walk through the forest 🌳")
                print("2. Take a boat along the river 🛶")
                print ("======================================================================")
            else:
                print("You can walk through the forest.")

            selection= input("\nPlease choose the path to return:\n1.Walk 🌳\n2.Boat 🚣‍♂️\n")       
            if selection == "boat" or selection == "2":
                print("You wear the life vest on the boat.")
                print("\n🎉 BONUS MISSION COMPLETED! You receive 10 extra points.")
                total= score (total)
                print(f"🎉 Congratulation! You completed the Save Forest adventure. Your score is {total}.")
                print ("======================================================================")
                break
            else:  
                print("You follow your map and compass.")
                print(f"🎉 Congratulation! You completed the Save Forest adventure. Your score is {total}.")
                break
                
    print("you stop the game")




