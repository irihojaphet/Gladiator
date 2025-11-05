def main():
    difficulty = input("Difficult or Casual? ")
    players = input("Multiplayer or Single-player? ")

    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend("Pocker")
        
        elif players == "Single player":
            recommend("Klondike")
        else:
            print("Choose between Multiplayer or Single-player")
            

    elif difficulty == "Casual":
        if players == "Multiplayer":
            recommend("Hearts")

        elif players == "Single player":
            recommend("Spider")

        else:
            print("Choose between Multiplayer or single player")

    else:
        print("Choose between Difficult or Casual")
         
     


def recommend(game):
    print("You might like ", game)

main()