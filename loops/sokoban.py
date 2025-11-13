def main():
    history = []

    while True:
        action = input("Action: ").capitalize()

        if action == "Undo":
            undone = history.pop()
            print(f"Undone{undone}")
        elif action == "Restart":
            history.clear()
            print("History cleared")
        elif action == "Quit":
            print("Exiting program")
            break
        else:
            history.append(action)
            print(history)

main()
