print ("======================================================================")
print("Please input your information:")
player_name = input("   - Name of gamer: ")
player_age = int(input("   - Age of gamer: "))
total = 0
bag = ["Water Bottom 🍶","Map 🗺️","Compass 🧭"]
print ("======================================================================")

if player_age < 6:
    print("You are a minor. The game is shutting down.")

else:
    print("\nHello! " + player_name)
    print("Welcome to save Forest ❤️")
    print("Your mission is to protect the forest and help the environment.")

    print("\nYou need to complete three environmental missions:")
    print("   - Mission 1: Water the tree 🌳")
    print("   - Mission 2: Collect plastic waste ♻️")
    print("   - Mission 3: Harvest the crops 🌾")

    print("\nTotal points that you can earn after completation all missons")
    print("   - Each mission gives you 10 points.")
    print("   - You can earn another 10 points by returning by boat.")
    print(" -> The maximum score is 40 points.")
    print ("======================================================================")
    main_menu = input("\n✅ Enter a command from the main menu:\n 1.explore\n 2.run\n 3.take\n 4.harvest\n 5.lopeta\n")

    def score (total):
        total = total + 10
        return total
    total= score(total)

    def inventory (items):
        for item in items:
            print(f"   - {item}")
        return items

    def explore(bag):
        print ("======================================================================")
        print("Let's start the adventure!")
        print(f"{player_name}, you are standing at the entrance of a beautiful forest")
        print("Before starting your journey, you receive an adventure bag.")
        new_item = input("What item would you like to pick up and add to your bag? ")
        print("\nCheck the items in your bag:")
        bag.append(new_item) 
        inventory (bag)

    def run(bag):
        print ("======================================================================")
        print(f"👉 You are standing under the tree. Now, find the 1st mission .")
        print("🌳 MISSION 1")
        print("The tree is very dry.")
        print("It needs water.")
        print("\n💧 You use your water to water the tree.")
        print("Wao! The tree looks healthy again! 🌳")
        print("Water Bottom 🍶 is no longer in the bag.")
        print("Check the items in your bag:")
        if "Water Bottom 🍶" in bag:
            bag.remove("Water Bottom 🍶")
        else:
            print("You don't have a Water Bottle in your bag, but you managed to find some water!")
        inventory (bag)


    def take(bag):
        print ("======================================================================")
        print("\n🌳 MISSION 2")
        print("You find a plastic bottle. Then take it and put it into your bag.")
        print("Goodjob! you contribute to clean the enviroment")
        item = input("What item do you want to collect? ")
        bag.append(item)
        
        print("Check the items in your bag:") 
        inventory (bag)

    def harvest(bag):
        print ("======================================================================")
        print("\n🌳 MISSION 3")
        print("you harvest the crops. Then take it and put it into your bag.")

        print("Check the items in your bag:")
        bag.append("Crops 🌾")  
        inventory (bag)

    while main_menu != "lopeta":
        if main_menu == "explore" or main_menu == "1":
            explore (bag)
            print("\nNow, open the bag and look at your map.")
            print("There is a big tree not far from here.")
            print("You have to RUN to the big tree for 1st mission.")
            print ("======================================================================")
            main_menu = input("\n✅ Enter a command from the main menu:\n1.explore\n2.run\n3.take\n4.harvest\n5.lopeta\n")

        elif main_menu == "run" or main_menu == "2":
            run(bag)
            total= score(total)

            print(f"🔅 Congratulation! You completed the 1st mission. Your score is {total}.")
            print ("======================================================================")
            main_menu = input("\n✅ Enter a command from the main menu:\n1.explore\n2.run\n3.take\n4.harvest\n5.lopeta\n")

        elif main_menu == "take" or main_menu == "3":
            take(bag)
            total= score(total)

            print(f"🔅 Congratulation! You completed the 2nd mission. Your score is {total}.")
            print ("======================================================================")
            main_menu = input("\n✅ Enter a command from the main menu:\n1.explore\n2.run\n3.take\n4.harvest\n5.lopeta\n")

        elif main_menu == "harvest" or main_menu == "4":
            harvest(bag)
            total= score(total)

            print(f"🔅 Congratulation! You completed the 3rd mission. Your score is {total}.")
            print ("======================================================================")
            print("\n🏁 Now you need to return to the starting point.")
            extra = input("Do you want to do extra mission? \n   - Yes\n   - No\n")
            if extra == "yes" or extra == "Yes" or extra == "y":
                print("\n💰 EXTRA MISSION")
                print("\nThere are two different routes:")
                print("   1. Walk through the forest 🌳")
                print("   2. Take a boat along the river 🛶")
                print("You can earn another 10 points by returning by boat.")
                print("======================================================================")
            else:
                print("You can go through the forest and walk to the starting point.")

            selection= input("\nNow is your choice, you can change your mind:\n   1.Walk 🌳\n   2.Boat 🛶\n")       
            if selection == "boat" or selection == "2":
                print("\n🛶 You choose the river route.")
                print("There is a life vest on the boat. Wear it and step on the boat")
                print("\nWhile travelling along the river,")
                print("You see plastic waste floating in the water.")
                print("\nYou collect the waste and help keep the river clean. ♻️")
                print("\n🎉 BONUS MISSION COMPLETED! You receive 10 extra points.")
                print(f"🎉 Congratulation! You completed the Save Forest adventure. Your score is {total}.")
                print ("======================================================================")
                break
            else:  
                print("You follow your map and compass then reach the starting point.")
                print(f"🎉 Congratulation! You completed the Save Forest adventure. Your score is {total}.")
                
            break

    print("You stop the game")




