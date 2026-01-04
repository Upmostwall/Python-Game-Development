import time
while True:
    games = {
        "Cricket": "A game played with a bat and ball",
        "Football": "A game played with a ball and two teams",
        "Chess": "A game played with pieces on a board"
    }

    print("-----Games Dictionary-----")
    print("1.Get Game Description")
    print("2.Add A New Game")
    print("3.Change Game Description")
    print("4.Delete A Game")
    print("5.Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        game = input("Enter the game name: ").lower()
        
        if game in games:
            print("Description:", games[game])
                                                         
        else:
            print("Game not found in dictionary.")
        
    elif choice == 2:
        new_game = input("Enter the game name: ").lower()
        description = input("Enter the game description: ")
        
        games[new_game] = description
        print("Game added successfully.")

    elif choice == 3:
        game = input("Enter the game name to change description: ").lower()
        
        if game in games:
            new_description = input("Enter the new description: ")
            games[game] = new_description
            print("Description updated successfully.")
        else:
            print("Game not found in dictionary.")

    elif choice == 4:
        game = input("Enter the game name to delete: ").lower()
        
        if game in games:
            del games[game]
            print("Game deleted successfully.")
        else:
            print("Game not found in dictionary.")
    
    elif choice == 5:
        print("Exiting the program.")
        time.sleep(2)
        break

    else:
        print("Invalid choice. Please select a valid option (1-4).")


    print("\n-----Updated Games Dictionary-----")
    print(games)