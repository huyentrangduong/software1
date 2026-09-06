player_name = input("name of gamer: ")
player_age = int(input("age of gamer: "))



if player_age < 12:
    print("You are a minor. The game is shutting down.")

else:
    print("\nHello!" + player_name)
    main_menu = input("\nEnter a command from the main menu:\nexplore\nrun\ntake\nharvest\nlopeta\n")

    while main_menu != "lopeta":
        main_menu = input("\nEnter a command from the main menu:\nexplore\nrun\ntake\nharvest\nlopeta\n")

        if main_menu == "explore":
            print("you explore the forest")
        
        elif main_menu == "run":
            print("you run to the big tree")

        elif main_menu == "take":
            print("you take some fruits")

        elif main_menu == "harvest":
            print("you harvest the crops")

    print("you stop the game")

