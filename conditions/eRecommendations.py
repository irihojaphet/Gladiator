def main():
    difficulty = input("Difficult or Casual? ")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Choose between Difficult or Casual")
        return

    players = input("Multiplayer or Single-player? ")
    if not (players == "Multiplayer" or players == "Single player"):
        print("Choose between Multiplayer or Single-player") 
        return

    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("Pocker")
        
    elif difficulty == "Difficult" and players == "Single player":
        recommend("Klondike")
            

    elif difficulty == "Casual" and players == "Multiplayer":
        recommend("Hearts")

    else:
        recommend("Spider")


def recommend(game):
    print("You might like ", game)

main()